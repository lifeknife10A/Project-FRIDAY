"""
PROJECT FRIDAY - TOKENIZER VOCABULARY SUBSET PRUNER
Author: Krishna Jagat Solanki
Goal: Extract a strict 64,000-token vocabulary subset V_S from Qwen2.5 (151,936 tokens)
preserving high-frequency English, Hindi/Devanagari, and conversational Hinglish tokens.
"""

import os
import json
import argparse

def generate_vocabulary_subset(target_vocab_size: int = 64000, output_path: str = None):
    """
    Simulates / defines the pruning policy for generating V_S:
    1. Mandatory preservation of all Special Tokens (<|im_start|>, <|im_end|>, etc.) [~500 tokens]
    2. Mandatory preservation of all raw single-byte tokens (UTF-8 bytes 0-255) [256 tokens]
    3. Mandatory preservation of Devanagari Unicode block (Hindi tokens) [~4,500 tokens]
    4. Frequency-ranked selection of common English & Hinglish BPE tokens [58,744 tokens]
    Total = Exactly 64,000 tokens.
    """
    print(f"Generating vocabulary subset configuration for |V_S| = {target_vocab_size} tokens...")
    
    spec = {
        "source_tokenizer": "Qwen/Qwen2.5-0.5B",
        "source_vocab_size": 151936,
        "target_vocab_size": target_vocab_size,
        "pruning_policy": {
            "special_tokens_reserved": 500,
            "raw_byte_tokens_reserved": 256,
            "devanagari_hindi_tokens_allocated": 4500,
            "english_hinglish_frequency_tokens_allocated": target_vocab_size - (500 + 256 + 4500)
        },
        "compression_ratio": round(target_vocab_size / 151936, 4),
        "lm_head_memory_footprint_int8_mb": round(target_vocab_size * 896 * 1.0 / 1e6, 2)
    }
    
    print(f"  Source Vocabulary: {spec['source_tokenizer']} ({spec['source_vocab_size']} tokens)")
    print(f"  Target Vocabulary: {spec['target_vocab_size']} tokens")
    print(f"  Vocabulary Compression: {spec['compression_ratio'] * 100:.2f}% of original")
    print(f"  LM-Head Memory Footprint (INT8): {spec['lm_head_memory_footprint_int8_mb']} MB (Down from 136.1 MB)")
    
    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w") as f:
            json.dump(spec, f, indent=2)
        print(f"Saved vocabulary pruning manifest to: {output_path}")

    return spec

if __name__ == "__main__":
    out_file = os.path.join(os.path.dirname(__file__), "../configs/vocab_subset_spec.json")
    generate_vocabulary_subset(target_vocab_size=64000, output_path=out_file)
