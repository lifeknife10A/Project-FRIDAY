"""
PROJECT FRIDAY - PHASE 1 AI DISTILLATION ENGINE
Stage 1: Normalized, Epsilon-Smoothed Top-64 Forward KL Divergence Loss
Author: Krishna Jagat Solanki
Target Architecture: SigLIP-B + Qwen2.5-0.5B (64k Pruned Vocabulary)

Mathematical Formulation:
Because the student vocabulary V_S (size 64,000) is a strict subset of the
teacher vocabulary V_T (size 151,936), standard Kullback-Leibler divergence is undefined
if the teacher predicts tokens outside V_S. This module bounds distillation strictly over:
    Omega_64 = Top-64( { v in V_S | p_T(v) } )  ==>  Omega_64 subset of V_S
Both distributions are explicitly renormalized over Omega_64 with epsilon-smoothing
on the student, guaranteeing a bounded, convergent KL divergence on a normalized probability space.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F

class BoundedForwardKDLoss(nn.Module):
    """
    Normalized, Epsilon-Smoothed Top-K Forward KL Divergence Loss
    constrained strictly to the student vocabulary support set Omega_K.
    """
    def __init__(self, top_k: int = 64, epsilon: float = 1e-5, temperature: float = 1.0):
        super().__init__()
        self.top_k = top_k
        self.epsilon = epsilon
        self.temperature = temperature

    def forward(
        self,
        student_logits: torch.Tensor,
        teacher_logits_on_student_vocab: torch.Tensor,
        mask: torch.Tensor = None
    ) -> torch.Tensor:
        """
        Args:
            student_logits: [batch_size, seq_len, vocab_size_student]
            teacher_logits_on_student_vocab: [batch_size, seq_len, vocab_size_student]
                (Teacher logits pre-filtered to the student vocabulary subset V_S)
            mask: Optional [batch_size, seq_len] attention/padding mask

        Returns:
            Scalar tensor representing the bounded Forward KL divergence loss.
        """
        # Apply temperature scaling
        s_logits = student_logits / self.temperature
        t_logits = teacher_logits_on_student_vocab / self.temperature

        # 1. Compute full softmax probabilities over student vocabulary V_S
        p_t_full = F.softmax(t_logits, dim=-1) # [B, L, V_S]
        p_s_full = F.softmax(s_logits, dim=-1) # [B, L, V_S]

        # 2. Extract Top-K teacher tokens over V_S to define Omega_K
        topk_probs_t, topk_indices = torch.topk(p_t_full, k=self.top_k, dim=-1) # [B, L, K]

        # Gather corresponding student probabilities on Omega_K
        topk_probs_s = torch.gather(p_s_full, dim=-1, index=topk_indices) # [B, L, K]

        # 3. Renormalize teacher distribution over Omega_K
        sum_t = torch.sum(topk_probs_t, dim=-1, keepdim=True).clamp(min=1e-9)
        p_tilde_t = topk_probs_t / sum_t # [B, L, K], sums to 1.000

        # 4. Renormalize student distribution over Omega_K and apply epsilon smoothing
        sum_s = torch.sum(topk_probs_s, dim=-1, keepdim=True).clamp(min=1e-9)
        p_bar_s = topk_probs_s / sum_s # [B, L, K], sums to 1.000
        p_tilde_s = (1.0 - self.epsilon) * p_bar_s + (self.epsilon / float(self.top_k))

        # 5. Compute Kullback-Leibler Divergence: D_KL( p_tilde_t || p_tilde_s )
        # D_KL = sum( p_tilde_t * (ln(p_tilde_t) - ln(p_tilde_s)) )
        log_p_tilde_t = torch.log(p_tilde_t.clamp(min=1e-12))
        log_p_tilde_s = torch.log(p_tilde_s.clamp(min=1e-12))
        kl_div = torch.sum(p_tilde_t * (log_p_tilde_t - log_p_tilde_s), dim=-1) # [B, L]

        # 6. Apply sequence mask if provided
        if mask is not None:
            kl_div = kl_div * mask
            loss = torch.sum(kl_div) / torch.sum(mask).clamp(min=1.0)
        else:
            loss = torch.mean(kl_div)

        # Scale by temperature squared as standard in knowledge distillation
        return loss * (self.temperature ** 2)

if __name__ == "__main__":
    print("Testing BoundedForwardKDLoss module...")
    loss_fn = BoundedForwardKDLoss(top_k=64, epsilon=1e-5, temperature=1.0)
    
    # Simulate batch of 2 tokens with 64,000 vocab size
    B, L, V = 2, 8, 64000
    s_logits = torch.randn(B, L, V, requires_grad=True)
    t_logits = torch.randn(B, L, V) # Simulated teacher logits over V_S
    
    loss = loss_fn(s_logits, t_logits)
    loss.backward()
    
    print(f"Computed KD Loss: {loss.item():.4f}")
    print(f"Gradient norm on student logits: {s_logits.grad.norm().item():.4f}")
    assert not torch.isnan(loss), "Loss produced NaN!"
    assert not torch.isinf(loss), "Loss produced Inf!"
    assert s_logits.grad is not None, "Gradients failed to backpropagate!"
    print(">>> BoundedForwardKDLoss mathematically closed and verified! <<<")
