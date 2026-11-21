"""
PROJECT FRIDAY - PHASE 1 AI TWO-STAGE DISTILLATION LOSS MODULE
Author: Krishna Jagat Solanki (Lead ML & Systems Engineer, Project FRIDAY)
Workspace: /Users/krish/NMIMS/Friday/phase1_ai_sandbox/

Stage 1: Normalized Epsilon-Smoothed Top-64 Forward KL Divergence Loss
Stage 2: Sequence Direct Preference Optimization (DPO) for Wearable Assistance

Mathematical Formulation:
Because the student vocabulary V_S (size 64,000) is a strict subset of the teacher
vocabulary V_T (size 151,643+), standard Kullback-Leibler divergence is undefined
if the teacher predicts tokens outside V_S.

Stage 1 (Bounded Forward KL):
1. Bound teacher candidates strictly to V_S:
   Omega_64 = Top-64( { v in V_S | p_T(v) } )  ==>  Omega_64 subset of V_S
2. Renormalize teacher probabilities over Omega_64:
   p_tilde_T(v) = p_T(v) / sum_{u in Omega_64} p_T(u)
3. Smooth student probabilities over Omega_64 with epsilon = 1e-5:
   p_tilde_S(v) = (p_S(v) + epsilon) / (1 + |Omega_64| * epsilon)
4. Forward KL divergence:
   L_KD = sum_{v in Omega_64} p_tilde_T(v) * log( p_tilde_T(v) / p_tilde_S(v) )

Stage 2 (Sequence DPO for Wearable Conciseness):
Directly optimizes policy pi_theta against frozen reference pi_ref to prefer
concise, first-person wearable assistance pairs (zero conversational pleasantries):
L_DPO = - E_{(x, y_w, y_l)} [ log sigma( beta * ( log(pi_theta(y_w|x)/pi_ref(y_w|x))
                                               - log(pi_theta(y_l|x)/pi_ref(y_l|x)) ) ) ]
"""

import os
import sys
from typing import Optional, Tuple, Dict, List
import torch
import torch.nn as nn
import torch.nn.functional as F


# ---------------------------------------------------------------------------
# STAGE 1: BOUNDED FORWARD KL DIVERGENCE LOSS
# ---------------------------------------------------------------------------

class BoundedForwardKDLoss(nn.Module):
    """
    Normalized, Epsilon-Smoothed Top-64 Forward KL Divergence Loss
    constrained strictly to the student vocabulary support set Omega_64 subset V_S.
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
        mask: Optional[torch.Tensor] = None
    ) -> torch.Tensor:
        """
        Args:
            student_logits: [batch_size, seq_len, 64000]
            teacher_logits_on_student_vocab: [batch_size, seq_len, 64000]
                (Teacher logits pre-filtered to the student vocabulary subset V_S)
            mask: Optional [batch_size, seq_len] attention/padding mask

        Returns:
            Scalar tensor representing the bounded Forward KL divergence loss.
        """
        # Apply temperature scaling
        s_logits = student_logits / self.temperature
        t_logits = teacher_logits_on_student_vocab / self.temperature

        # 1. Full softmax probabilities over student vocabulary V_S (size 64000)
        p_t_full = F.softmax(t_logits, dim=-1)  # [B, L, 64000]
        p_s_full = F.softmax(s_logits, dim=-1)  # [B, L, 64000]

        # 2. Extract Top-K teacher candidates over V_S to define Omega_K
        topk_probs_t, topk_indices = torch.topk(p_t_full, k=self.top_k, dim=-1)  # [B, L, K]

        # Gather corresponding student probabilities on Omega_K
        topk_probs_s = torch.gather(p_s_full, dim=-1, index=topk_indices)  # [B, L, K]

        # 3. Renormalize teacher distribution over Omega_K
        sum_t = torch.sum(topk_probs_t, dim=-1, keepdim=True).clamp(min=1e-12)
        p_tilde_t = topk_probs_t / sum_t  # [B, L, K], strictly sums to 1.0

        # 4. Smooth student probabilities over Omega_K with epsilon = 1e-5
        # Formula: p_tilde_S(v) = (p_S(v) + epsilon) / (1 + |Omega_K| * epsilon)
        # Note: If student probabilities on Omega_K are first normalized or raw:
        # Prompt invariant: \tilde{p}_S(v) = (p_S(v) + \epsilon) / (1 + |\Omega_{64}|\epsilon)
        # To maintain exact probability space on Omega_K:
        sum_s = torch.sum(topk_probs_s, dim=-1, keepdim=True).clamp(min=1e-12)
        norm_probs_s = topk_probs_s / sum_s
        p_tilde_s = (norm_probs_s + self.epsilon) / (1.0 + float(self.top_k) * self.epsilon)

        # 5. Forward-KL loss: L_KD = sum_{v in Omega_K} p_tilde_T(v) * log( p_tilde_T(v) / p_tilde_S(v) )
        log_p_tilde_t = torch.log(p_tilde_t.clamp(min=1e-12))
        log_p_tilde_s = torch.log(p_tilde_s.clamp(min=1e-12))
        kl_div = torch.sum(p_tilde_t * (log_p_tilde_t - log_p_tilde_s), dim=-1)  # [B, L]

        # 6. Apply sequence mask if provided
        if mask is not None:
            kl_div = kl_div * mask
            loss = torch.sum(kl_div) / torch.sum(mask).clamp(min=1.0)
        else:
            loss = torch.mean(kl_div)

        # Scale by temperature squared as standard in knowledge distillation
        return loss * (self.temperature ** 2)


# ---------------------------------------------------------------------------
# STAGE 2: SEQUENCE DIRECT PREFERENCE OPTIMIZATION (DPO) LOSS
# ---------------------------------------------------------------------------

class SequenceDPOLoss(nn.Module):
    """
    Sequence Direct Preference Optimization (DPO) Loss for Project FRIDAY:
    Aligns student VLM on concise, first-person wearable assistance pairs
    (eliminates AI pleasantries, greetings, and boilerplate disclosures).
    """
    def __init__(self, beta: float = 0.1, label_smoothing: float = 0.0):
        super().__init__()
        self.beta = beta
        self.label_smoothing = label_smoothing

    def forward(
        self,
        policy_chosen_logps: torch.Tensor,
        policy_rejected_logps: torch.Tensor,
        reference_chosen_logps: torch.Tensor,
        reference_rejected_logps: torch.Tensor
    ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        """
        Computes the standard DPO loss:
            pi_logratios = policy_chosen_logps - policy_rejected_logps
            ref_logratios = reference_chosen_logps - reference_rejected_logps
            logits = self.beta * (pi_logratios - ref_logratios)
            loss = -log_sigmoid(logits)

        Args:
            policy_chosen_logps: [B] log pi_theta(y_w | x)
            policy_rejected_logps: [B] log pi_theta(y_l | x)
            reference_chosen_logps: [B] log pi_ref(y_w | x)
            reference_rejected_logps: [B] log pi_ref(y_l | x)

        Returns:
            Tuple of (loss, chosen_rewards, rejected_rewards)
        """
        pi_logratios = policy_chosen_logps - policy_rejected_logps
        ref_logratios = reference_chosen_logps - reference_rejected_logps

        logits = self.beta * (pi_logratios - ref_logratios)

        if self.label_smoothing > 0.0:
            loss = (
                -F.logsigmoid(logits) * (1.0 - self.label_smoothing)
                - F.logsigmoid(-logits) * self.label_smoothing
            ).mean()
        else:
            loss = -F.logsigmoid(logits).mean()

        chosen_rewards = self.beta * (policy_chosen_logps - reference_chosen_logps).detach()
        rejected_rewards = self.beta * (policy_rejected_logps - reference_rejected_logps).detach()

        return loss, chosen_rewards, rejected_rewards

    @staticmethod
    def compute_sequence_logps(
        logits: torch.Tensor,
        labels: torch.Tensor,
        label_mask: Optional[torch.Tensor] = None
    ) -> torch.Tensor:
        """
        Computes total log probability of token sequences given model logits.
        Args:
            logits: [B, L, V]
            labels: [B, L]
            label_mask: [B, L] 1 for target tokens, 0 for prompt/padding
        Returns:
            seq_logps: [B] sum of log probabilities for labeled tokens
        """
        log_probs = F.log_softmax(logits, dim=-1)
        per_token_logps = torch.gather(log_probs, dim=-1, index=labels.unsqueeze(-1)).squeeze(-1)

        if label_mask is not None:
            per_token_logps = per_token_logps * label_mask
            seq_logps = per_token_logps.sum(dim=-1)
        else:
            seq_logps = per_token_logps.sum(dim=-1)

        return seq_logps


# ---------------------------------------------------------------------------
# WEARABLE PREFERENCE DATASET SAMPLES (ZERO PLEASANTRIES CONTRACT)
# ---------------------------------------------------------------------------

WEARABLE_PREFERENCE_DATASET = [
    {
        "prompt": "<|vision_start|>[FOVEAL_IMAGE]<|vision_end|> What are the dosage instructions on this prescription bottle?",
        "chosen": "Amoxicillin 500mg. Take 1 capsule twice daily with meals for 10 days. Warning: finish all medication. 20 capsules, zero refills.",
        "rejected": "Hello! As an AI smart glasses assistant, I would be happy to help you read that prescription label. Looking closely at the bottle in front of you, the medication is Amoxicillin 500 milligrams..."
    },
    {
        "prompt": "<|vision_start|>[FOVEAL_IMAGE]<|vision_end|> What is in front of me?",
        "chosen": "MacBook Air on a wooden desk with a prescription bottle and coffee mug to the right.",
        "rejected": "Certainly! Looking through your camera right now, I can see what appears to be a modern laptop computer placed on top of a wooden desk..."
    },
    {
        "prompt": "<|vision_start|>[FOVEAL_IMAGE]<|vision_end|> Can you search for nearby pharmacies?",
        "chosen": "Offline. No network connection. Connect Wi-Fi or tether to phone to search.",
        "rejected": "I apologize, but I am unable to perform a web search right now because I don't have an active internet connection. Please connect your device..."
    }
]


# ---------------------------------------------------------------------------
# COMBINED TWO-STAGE DISTILLATION LOSS MODULE
# ---------------------------------------------------------------------------

class FridayTwoStageDistillationLoss(nn.Module):
    """
    Unified Two-Stage Objective for Project FRIDAY:
      L_total = alpha_kd * L_BoundedKD + alpha_dpo * L_DPO
    """
    def __init__(
        self,
        top_k: int = 64,
        epsilon: float = 1e-5,
        kd_temperature: float = 1.0,
        dpo_beta: float = 0.1,
        alpha_kd: float = 1.0,
        alpha_dpo: float = 0.5
    ):
        super().__init__()
        self.stage1_kd = BoundedForwardKDLoss(top_k=top_k, epsilon=epsilon, temperature=kd_temperature)
        self.stage2_dpo = SequenceDPOLoss(beta=dpo_beta)
        self.alpha_kd = alpha_kd
        self.alpha_dpo = alpha_dpo

    def forward_kd(
        self,
        student_logits: torch.Tensor,
        teacher_logits: torch.Tensor,
        mask: Optional[torch.Tensor] = None
    ) -> torch.Tensor:
        return self.stage1_kd(student_logits, teacher_logits, mask)

    def forward_dpo(
        self,
        policy_chosen_logps: torch.Tensor,
        policy_rejected_logps: torch.Tensor,
        reference_chosen_logps: torch.Tensor,
        reference_rejected_logps: torch.Tensor
    ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        return self.stage2_dpo(
            policy_chosen_logps,
            policy_rejected_logps,
            reference_chosen_logps,
            reference_rejected_logps
        )


# ---------------------------------------------------------------------------
# UNIT TESTS & AUDIT SUITE
# ---------------------------------------------------------------------------

def run_tests():
    print("==================================================================")
    print("PROJECT FRIDAY: TWO-STAGE DISTILLATION LOSS AUDIT")
    print("==================================================================")

    # 1. Test Stage 1: Bounded Top-64 Forward KL Loss
    print("--- [STAGE 1] Testing BoundedForwardKDLoss Module ---")
    kd_loss_fn = BoundedForwardKDLoss(top_k=64, epsilon=1e-5, temperature=1.0)

    B, L, V = 2, 8, 64000
    s_logits = torch.randn(B, L, V, requires_grad=True)
    t_logits = torch.randn(B, L, V)
    mask = torch.ones(B, L)

    kd_loss = kd_loss_fn(s_logits, t_logits, mask=mask)
    kd_loss.backward()

    print(f"  Computed Stage 1 KD Loss: {kd_loss.item():.4f}")
    print(f"  Student Logits Grad Norm: {s_logits.grad.norm().item():.4f}")

    assert not torch.isnan(kd_loss), "Stage 1 KD Loss is NaN!"
    assert not torch.isinf(kd_loss), "Stage 1 KD Loss is Inf!"
    assert kd_loss.item() > 0.0, "Stage 1 KD Loss must be positive"
    assert s_logits.grad is not None, "Gradients failed to backpropagate!"
    print("  [PASS] Stage 1 Normalized Epsilon-Smoothed Top-64 Forward KL Divergence verified")

    # 2. Test Stage 2: Sequence Direct Preference Optimization (DPO)
    print("\n--- [STAGE 2] Testing SequenceDPOLoss Module ---")
    dpo_loss_fn = SequenceDPOLoss(beta=0.1)

    # Simulate log-probabilities for 4 preference pairs
    B_dpo = 4
    # Policy prefers chosen sequences (higher logp for chosen, lower for rejected)
    pi_chosen_logp = torch.tensor([-12.5, -14.0, -10.2, -15.1], requires_grad=True)
    pi_rejected_logp = torch.tensor([-25.0, -28.2, -22.4, -30.0], requires_grad=True)
    ref_chosen_logp = torch.tensor([-15.0, -16.0, -12.0, -17.0])
    ref_rejected_logp = torch.tensor([-18.0, -19.0, -15.0, -20.0])

    dpo_loss, chosen_rew, rej_rew = dpo_loss_fn(
        pi_chosen_logp,
        pi_rejected_logp,
        ref_chosen_logp,
        ref_rejected_logp
    )
    dpo_loss.backward()

    print(f"  Computed Stage 2 DPO Loss: {dpo_loss.item():.4f}")
    print(f"  Chosen Rewards Mean: {chosen_rew.mean().item():.4f}")
    print(f"  Rejected Rewards Mean: {rej_rew.mean().item():.4f}")
    print(f"  Policy Chosen Grad Norm: {pi_chosen_logp.grad.norm().item():.4f}")

    assert not torch.isnan(dpo_loss), "Stage 2 DPO Loss is NaN!"
    assert not torch.isinf(dpo_loss), "Stage 2 DPO Loss is Inf!"
    assert chosen_rew.mean() > rej_rew.mean(), "Chosen reward must exceed rejected reward"
    print("  [PASS] Stage 2 Sequence DPO Objective verified")

    # 3. Test Log-Prob Computation Helper
    print("\n--- Testing Sequence Log-Probability Computation ---")
    seq_logits = torch.randn(2, 6, 64000, requires_grad=True)
    seq_labels = torch.randint(0, 64000, (2, 6))
    seq_mask = torch.tensor([[1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 0]], dtype=torch.float32)

    computed_logps = SequenceDPOLoss.compute_sequence_logps(seq_logits, seq_labels, seq_mask)
    assert computed_logps.shape == (2,), f"Unexpected logps shape: {computed_logps.shape}"
    assert not torch.isnan(computed_logps).any(), "NaN found in computed logps"
    print(f"  Computed Sequence LogPs: {computed_logps.detach().numpy()}")
    print("  [PASS] Sequence log-probability extraction verified")

    # 4. Verify Wearable Preference Dataset Samples
    assert len(WEARABLE_PREFERENCE_DATASET) >= 3
    for pair in WEARABLE_PREFERENCE_DATASET:
        assert len(pair["chosen"]) < len(pair["rejected"]), "Chosen must be concise relative to rejected"
        assert not any(p in pair["chosen"].lower() for p in ["hello", "as an ai", "i would be happy"]), (
            "Chosen text must have zero conversational pleasantries"
        )
    print("  [PASS] Wearable assistance preference pairs verified (zero pleasantries)")

    print("==================================================================")
    print("ALL TESTS PASSED [✓]")
    print("==================================================================")


if __name__ == "__main__":
    run_tests()
