"""
PROJECT FRIDAY - STUDENT VISION-LANGUAGE MODEL ARCHITECTURE
Component: SigLIP-B Vision Encoder + 2x2 Spatial Unshuffle Downsampler + Qwen2.5-0.5B Decoder
Author: Krishna Jagat Solanki
"""

import math
import torch
import torch.nn as nn
import torch.nn.functional as F

class SpatialUnshuffleDownsampler(nn.Module):
    """
    Downsamples a 2D patch grid by a factor of 2x2 using spatial unshuffle,
    compressing 576 visual tokens (24x24 grid) into exactly 144 tokens (12x12 grid).
    This reduces vision prefix length by 75% to fit within the 9.36 GB/s memory bandwidth budget.
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
        out_tokens = self.projector(x_seq) # [B, 144, 896]
        return out_tokens

class FridayStudentVLM(nn.Module):
    """
    Complete Student VLM pipeline for Project FRIDAY:
    1. Ingests 384x384 image frame.
    2. Encodes via SigLIP-B patch embeddings (576 patches).
    3. Compresses to 144 visual tokens via SpatialUnshuffleDownsampler.
    4. Prepends visual tokens to conversational text token embeddings.
    """
    def __init__(self, visual_dim: int = 768, hidden_dim: int = 896, vocab_size: int = 64000):
        super().__init__()
        self.vocab_size = vocab_size
        self.hidden_dim = hidden_dim
        
        # 1. 2x2 Spatial Unshuffle Downsampler
        self.unshuffle_projector = SpatialUnshuffleDownsampler(
            in_features=visual_dim,
            out_features=hidden_dim,
            grid_size=24
        )
        
        # 2. Text token embedding layer for the 64k vocabulary subset
        self.token_embeddings = nn.Embedding(vocab_size, hidden_dim)
        
        # 3. Simulated/Placeholder decoder head (in full training, wraps Qwen2.5-0.5B decoder)
        self.lm_head = nn.Linear(hidden_dim, vocab_size, bias=False)

    def forward(
        self,
        simulated_patch_embeddings: torch.Tensor,
        input_ids: torch.Tensor
    ) -> torch.Tensor:
        """
        Args:
            simulated_patch_embeddings: [B, 576, 768] (from SigLIP-B)
            input_ids: [B, L] token ids in [0, 63999]
        Returns:
            logits: [B, 144 + L, vocab_size]
        """
        # Compress 576 visual tokens to 144 tokens
        visual_tokens = self.unshuffle_projector(simulated_patch_embeddings) # [B, 144, 896]
        
        # Embed text tokens
        text_tokens = self.token_embeddings(input_ids) # [B, L, 896]
        
        # Concatenate multimodal prefix
        multimodal_sequence = torch.cat([visual_tokens, text_tokens], dim=1) # [B, 144 + L, 896]
        
        # Project to vocabulary logits
        logits = self.lm_head(multimodal_sequence)
        return logits

if __name__ == "__main__":
    print("Testing FridayStudentVLM and SpatialUnshuffleDownsampler...")
    model = FridayStudentVLM(visual_dim=768, hidden_dim=896, vocab_size=64000)
    
    # Simulate batch of 2 images and 16 text tokens
    B = 2
    raw_patches = torch.randn(B, 576, 768)
    text_ids = torch.randint(0, 64000, (B, 16))
    
    logits = model(raw_patches, text_ids)
    print(f"Input Patches Shape: {raw_patches.shape}")
    print(f"Output Logits Shape: {logits.shape}")
    
    assert logits.shape == (2, 144 + 16, 64000), f"Unexpected output shape: {logits.shape}"
    print(">>> 576 -> 144 Token Spatial Unshuffle verified successfully! <<<")
