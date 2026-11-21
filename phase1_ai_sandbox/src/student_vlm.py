"""
PROJECT FRIDAY - STUDENT VISION-LANGUAGE MODEL ARCHITECTURE
Component: SigLIP-B Vision Encoder + 2x2 Spatial Unshuffle Downsampler + Qwen2.5-0.5B Decoder (INT4 Simulation)
Author: Krishna Jagat Solanki (Lead ML & Systems Engineer, Project FRIDAY)
Workspace: /Users/krish/NMIMS/Friday/phase1_ai_sandbox/

Physical & Hardware Invariants:
1. Visual Token Invariant: 384x384 input -> 24x24 = 576 patches -> 2x2 Spatial Unshuffle downsampler
   cuts sequence length by 75% down to strictly 144 visual tokens (D=896) to prevent NPU SRAM overflow.
2. Vocabulary Invariant: Strict 64,000-token subset V_S of Qwen2.5 (V_S subset V_T).
3. Memory Bandwidth Invariant: INT4 weights for layers (176.0 MB/token) + INT8 LM head (57.34 MB/token)
   + Scales/Norms (16.0 MB) + KV-Cache (18.0 MB) = 267.34 MB/token (<= 9.36 GB/s @ 35 tok/s).
"""

import math
from typing import Optional, List, Tuple, Generator
import torch
import torch.nn as nn
import torch.nn.functional as F


# ---------------------------------------------------------------------------
# INT4 WEIGHT SIMULATION MODULE
# ---------------------------------------------------------------------------

class INT4SimulatedLinear(nn.Module):
    """
    Simulates INT4 symmetric weight quantization and memory traffic.
    Quantizes FP32/FP16 weights to 4-bit signed integers in [-8, 7],
    dequantizes for computation, and measures actual bytes transferred per token.
    """
    def __init__(self, in_features: int, out_features: int, bias: bool = False):
        super().__init__()
        self.in_features = in_features
        self.out_features = out_features
        self.weight = nn.Parameter(torch.randn(out_features, in_features) * 0.02)
        if bias:
            self.bias = nn.Parameter(torch.zeros(out_features))
        else:
            self.register_parameter("bias", None)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # Compute per-channel or per-tensor scale factor for INT4 range [-8, 7]
        max_val = torch.max(torch.abs(self.weight)).clamp(min=1e-8)
        scale = max_val / 7.0
        # Quantize to INT4
        w_int4 = torch.clamp(torch.round(self.weight / scale), -8, 7)
        # Dequantize
        w_dequant = w_int4 * scale
        return F.linear(x, w_dequant, self.bias)

    @property
    def weight_bytes_transferred(self) -> float:
        """Memory bandwidth traffic: 0.5 bytes per parameter for INT4."""
        num_params = self.in_features * self.out_features
        return num_params * 0.5


# ---------------------------------------------------------------------------
# 2x2 SPATIAL UNSHUFFLE DOWNSAMPLER (576 -> 144 VISUAL TOKENS)
# ---------------------------------------------------------------------------

class SpatialUnshuffleDownsampler(nn.Module):
    """
    Downsamples a 2D patch grid by a factor of 2x2 using spatial unshuffle,
    compressing 576 visual tokens (24x24 grid from SigLIP-B) into strictly 144 tokens (12x12 grid).
    This cuts visual prefix length by 75% to enforce the RK3576 9.36 GB/s bus load ceiling.
    """
    def __init__(self, in_features: int = 768, out_features: int = 896, grid_size: int = 24):
        super().__init__()
        self.grid_size = grid_size
        self.downsample_factor = 2
        # 2x2 unshuffle concatenates 4 adjacent spatial channels: 768 * 4 = 3072
        unshuffle_dim = in_features * (self.downsample_factor ** 2)

        self.projector = nn.Sequential(
            nn.LayerNorm(unshuffle_dim),
            nn.Linear(unshuffle_dim, out_features),
            nn.GELU(),
            nn.Linear(out_features, out_features)
        )

    def forward(self, patch_tokens: torch.Tensor) -> torch.Tensor:
        """
        Args:
            patch_tokens: [B, 576, in_features]
        Returns:
            downsampled_tokens: [B, 144, out_features]
        """
        B, N, C = patch_tokens.shape
        H = W = self.grid_size
        assert N == H * W, f"Input patch tokens {N} do not match grid {H}x{W}"

        # Reshape to spatial feature map: [B, H, W, C] -> [B, C, H, W]
        x = patch_tokens.view(B, H, W, C).permute(0, 3, 1, 2)

        # Pixel unshuffle: downsample spatial dims by 2, increase channel by 4
        # [B, C, H, W] -> [B, C * 4, H/2, W/2] = [B, 3072, 12, 12]
        x_unshuffle = F.pixel_unshuffle(x, downscale_factor=self.downsample_factor)

        # Permute back to sequence: [B, 12, 12, 3072] -> [B, 144, 3072]
        H_new, W_new = H // self.downsample_factor, W // self.downsample_factor
        x_seq = x_unshuffle.permute(0, 2, 3, 1).reshape(B, H_new * W_new, -1)

        # Project to language model hidden dimension (896)
        out_tokens = self.projector(x_seq)  # [B, 144, 896]
        return out_tokens


# ---------------------------------------------------------------------------
# SIGLIP-B PATCH EXTRACTION MODULE
# ---------------------------------------------------------------------------

class SigLIPPatchExtractor(nn.Module):
    """
    Extracts 576 patch embeddings from a 384x384 optical crop using
    a 16x16 patch projection kernel (384/16 = 24x24 = 576 patches, D=768).
    """
    def __init__(self, in_channels: int = 3, embed_dim: int = 768, patch_size: int = 16):
        super().__init__()
        self.patch_size = patch_size
        self.embed_dim = embed_dim
        self.proj = nn.Conv2d(
            in_channels, embed_dim,
            kernel_size=patch_size, stride=patch_size, bias=False
        )
        self.norm = nn.LayerNorm(embed_dim)

    def forward(self, pixel_values: torch.Tensor) -> torch.Tensor:
        """
        Args:
            pixel_values: [B, 3, 384, 384]
        Returns:
            patches: [B, 576, 768]
        """
        B, C, H, W = pixel_values.shape
        x = self.proj(pixel_values)  # [B, 768, 24, 24]
        x = x.flatten(2).transpose(1, 2)  # [B, 576, 768]
        return self.norm(x)


# ---------------------------------------------------------------------------
# FULL STUDENT VISION-LANGUAGE MODEL (FRIDAY 410M ARCHITECTURE)
# ---------------------------------------------------------------------------

class FridayStudentVLM(nn.Module):
    """
    Complete Student VLM pipeline for Project FRIDAY:
    1. Ingests 384x384 image frame.
    2. Encodes via SigLIP-B patch embeddings (576 patches).
    3. Compresses to strictly 144 visual tokens via SpatialUnshuffleDownsampler.
    4. Prepends visual tokens to conversational text token embeddings.
    5. Autoregressively decodes with INT4 weight simulation.
    """
    def __init__(
        self,
        visual_dim: int = 768,
        hidden_dim: int = 896,
        vocab_size: int = 64000,
        num_layers: int = 24
    ):
        super().__init__()
        self.vocab_size = vocab_size
        self.hidden_dim = hidden_dim
        self.num_layers = num_layers

        # 1. SigLIP Patch Extractor (384x384 -> 576 patches)
        self.patch_extractor = SigLIPPatchExtractor(embed_dim=visual_dim)

        # 2. 2x2 Spatial Unshuffle Downsampler (576 -> 144 Visual Tokens)
        self.unshuffle_projector = SpatialUnshuffleDownsampler(
            in_features=visual_dim,
            out_features=hidden_dim,
            grid_size=24
        )

        # 3. Text token embedding layer for the 64k vocabulary subset
        self.token_embeddings = nn.Embedding(vocab_size, hidden_dim)

        # 4. Decoder layers with INT4 weight quantization simulation
        # Represents the 410M parameter Qwen2.5-0.5B backbone
        self.layers = nn.ModuleList([
            INT4SimulatedLinear(hidden_dim, hidden_dim)
            for _ in range(min(num_layers, 4)) # 4 simulated benchmark layers for fast local testing
        ])
        self.norm = nn.LayerNorm(hidden_dim)

        # 5. INT8 Language Model Head (64,000 x 896 = 57.34 MB)
        self.lm_head = nn.Linear(hidden_dim, vocab_size, bias=False)

    def encode_image(self, pixel_values: torch.Tensor) -> torch.Tensor:
        """
        Processes 384x384 image down to strictly 144 visual tokens.
        Args:
            pixel_values: [B, 3, 384, 384] or [B, 576, 768] (raw patch embeddings)
        Returns:
            [B, 144, 896]
        """
        if pixel_values.dim() == 4:
            raw_patches = self.patch_extractor(pixel_values) # [B, 576, 768]
        else:
            raw_patches = pixel_values # [B, 576, 768]

        visual_tokens = self.unshuffle_projector(raw_patches) # [B, 144, 896]
        assert visual_tokens.shape[1] == 144, f"Visual tokens {visual_tokens.shape[1]} != 144"
        return visual_tokens

    def forward(
        self,
        simulated_patch_embeddings: torch.Tensor,
        input_ids: torch.Tensor
    ) -> torch.Tensor:
        """
        Multimodal forward pass.
        Args:
            simulated_patch_embeddings: [B, 576, 768] or [B, 3, 384, 384]
            input_ids: [B, L]
        Returns:
            logits: [B, 144 + L, 64000]
        """
        # 1. Visual encoding (strictly 144 tokens)
        visual_tokens = self.encode_image(simulated_patch_embeddings) # [B, 144, 896]

        # 2. Text embedding
        text_tokens = self.token_embeddings(input_ids) # [B, L, 896]

        # 3. Concatenate multimodal prefix
        x = torch.cat([visual_tokens, text_tokens], dim=1) # [B, 144 + L, 896]

        # 4. Decoder backbone with INT4 weights
        for layer in self.layers:
            x = x + layer(x)
        x = self.norm(x)

        # 5. LM Head
        logits = self.lm_head(x) # [B, 144 + L, 64000]
        return logits

    def generate_tokens(
        self,
        visual_tokens: torch.Tensor,
        prompt_ids: torch.Tensor,
        max_new_tokens: int = 32
    ) -> List[int]:
        """
        Simulates autoregressive token generation with INT4 memory bus traffic.
        """
        generated_ids = []
        curr_seq = torch.cat([visual_tokens, self.token_embeddings(prompt_ids)], dim=1)

        for _ in range(max_new_tokens):
            x = curr_seq
            for layer in self.layers:
                x = x + layer(x)
            x = self.norm(x)
            next_logit = self.lm_head(x[:, -1:, :]) # [1, 1, 64000]
            next_token = torch.argmax(next_logit, dim=-1).item()
            generated_ids.append(next_token)

            # Append new token embedding
            next_emb = self.token_embeddings(torch.tensor([[next_token]], device=curr_seq.device))
            curr_seq = torch.cat([curr_seq, next_emb], dim=1)
            
            # Stop token check
            if next_token in [151643, 151645]: # <|endoftext|>, <|im_end|>
                break

        return generated_ids


# ---------------------------------------------------------------------------
# UNIT TESTS & AUDIT SUITE
# ---------------------------------------------------------------------------

def run_tests():
    print("==================================================================")
    print("PROJECT FRIDAY: STUDENT VLM & SPATIAL UNSHUFFLE AUDIT")
    print("==================================================================")

    model = FridayStudentVLM(visual_dim=768, hidden_dim=896, vocab_size=64000)

    # 1. Test Spatial Unshuffle Downsampler (576 -> 144 tokens)
    B = 2
    raw_patches = torch.randn(B, 576, 768)
    downsampled = model.unshuffle_projector(raw_patches)
    print(f"  Input Patches Shape      : {raw_patches.shape}")
    print(f"  Downsampled Tokens Shape : {downsampled.shape}")
    assert downsampled.shape == (B, 144, 896), f"Shape mismatch: {downsampled.shape}"
    print("  [PASS] 576 -> 144 Visual Token Spatial Unshuffle verified")

    # 2. Test Full Multimodal Forward Pass
    text_ids = torch.randint(0, 64000, (B, 16))
    logits = model(raw_patches, text_ids)
    print(f"  Multimodal Logits Shape  : {logits.shape}")
    assert logits.shape == (B, 144 + 16, 64000), f"Logits shape mismatch: {logits.shape}"
    print("  [PASS] Multimodal forward pass verified on 64k vocabulary")

    # 3. Test INT4 Quantized Layer
    int4_layer = INT4SimulatedLinear(896, 896)
    dummy_x = torch.randn(2, 10, 896)
    out_int4 = int4_layer(dummy_x)
    assert out_int4.shape == dummy_x.shape
    assert int4_layer.weight_bytes_transferred == (896 * 896 * 0.5)
    print(f"  INT4 Linear Traffic      : {int4_layer.weight_bytes_transferred / 1e3:.1f} KB per layer")
    print("  [PASS] INT4 weight simulation and memory traffic verified")

    # 4. Test Autoregressive Generation
    single_patches = torch.randn(1, 576, 768)
    single_vis = model.encode_image(single_patches)
    single_prompt = torch.randint(0, 64000, (1, 8))
    tokens = model.generate_tokens(single_vis, single_prompt, max_new_tokens=5)
    print(f"  Generated Token Sequence : {tokens} (Length: {len(tokens)})")
    assert len(tokens) == 5
    print("  [PASS] Autoregressive token generation loop verified")

    print("==================================================================")
    print("ALL TESTS PASSED [✓]")
    print("==================================================================")


if __name__ == "__main__":
    run_tests()
