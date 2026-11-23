"""
PROJECT FRIDAY: SPEC-RESOLUTION HELD-OUT TEST SET BUILDER (Auditor Item F0)
Re-renders the 20-sample held-out test set at camera optical spec resolution (12.8 +/- 1 px/char):
- test_01 to test_06: re-rendered from build_verified_prescription_dataset.py specs
- test_07 to test_20: re-rendered from test_specs.json using render_photographic_benchmark_sample
Preserves 100% identical ground truth, prompts, and required_fields.
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json
import hashlib
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from scripts.build_benchmark_dataset import DEFAULT_PINNED_FONT_PATH, render_photographic_benchmark_sample
from scripts.build_verified_prescription_dataset import PRESCRIPTION_SPECS

def render_prescription_spec(spec, output_path, font_path=DEFAULT_PINNED_FONT_PATH, font_size=21):
    w, h = 1500, 960
    font = ImageFont.truetype(font_path, font_size)
    img = Image.new("RGB", (w, h), color=(253, 253, 251))
    draw = ImageDraw.Draw(img)

    # Frame border
    draw.rectangle([16, 16, w - 16, h - 16], outline=(160, 160, 160), width=4)
    # Header bar
    draw.rectangle([16, 16, w - 16, 140], fill=(210, 35, 45))
    draw.text((50, 36), spec["pharmacy"], font=font, fill=(255, 255, 255))
    draw.text((50, 80), spec["pharm_address"], font=font, fill=(255, 255, 255))

    # Rx & Patient block
    draw.text((50, 170), f"{spec['rx_num']}   DATE: {spec['date']}", font=font, fill=(20, 20, 20))
    draw.text((50, 224), spec["patient"], font=font, fill=(20, 20, 20))
    draw.text((50, 276), spec["doctor"], font=font, fill=(20, 20, 20))

    # Prominent medication line
    draw.line([40, 340, w - 40, 340], fill=(200, 200, 200), width=2)
    draw.text((50, 370), spec["drug_line"], font=font, fill=(0, 0, 0))
    draw.line([40, 440, w - 40, 440], fill=(200, 200, 200), width=2)

    # Directions
    draw.text((50, 470), spec["directions"], font=font, fill=(10, 10, 10))
    draw.text((50, 550), spec["warning"], font=font, fill=(90, 90, 90))

    # Qty, refills, NDC
    draw.text((50, 650), spec["qty_refills"], font=font, fill=(20, 20, 20))
    draw.text((50, 720), spec["ndc_mfr"], font=font, fill=(40, 40, 40))

    footer_text = spec.get("footer", "KEEP OUT OF REACH OF CHILDREN - FOR ORAL USE ONLY")
    draw.text((50, 820), footer_text, font=font, fill=(140, 20, 20))

    lines = [
        spec["pharmacy"], spec["pharm_address"],
        f"{spec['rx_num']}   DATE: {spec['date']}",
        spec["patient"], spec["doctor"],
        spec["drug_line"], spec["directions"], spec["warning"],
        spec["qty_refills"], spec["ndc_mfr"], footer_text
    ]
    all_line_widths = []
    all_line_chars = []
    for line in lines:
        if not line:
            continue
        bbox = draw.textbbox((0, 0), line, font=font)
        all_line_widths.append(bbox[2] - bbox[0])
        all_line_chars.append(len(line))
    measured_px_per_char = sum(all_line_widths) / sum(all_line_chars)

    img = img.filter(ImageFilter.GaussianBlur(radius=0.4))
    img.save(output_path, quality=95)
    return output_path, measured_px_per_char

def build_spec_testset(output_dir="assets/benchmark_testset_spec"):
    images_dir = os.path.join(output_dir, "images")
    os.makedirs(images_dir, exist_ok=True)

    with open("assets/benchmark_testset/test_specs.json") as f:
        test_specs = json.load(f)

    with open("assets/benchmark_testset/test_manifest.json") as f:
        orig_test_manifest = json.load(f)

    rx_indices = [7, 9, 12, 13, 17, 19]  # Losartan, Sertraline, Escitalopram, Acetaminophen, Pantoprazole, Prednisone
    
    print(f"[*] Building 20-Sample Held-Out Test Set (Spec Resolution, 12.8 px/char) in {output_dir}...")
    manifest = []
    logged_px_chars = []

    for idx, spec in enumerate(test_specs):
        tid = spec["id"]
        fname = f"{tid}.jpg"
        fpath = os.path.join(images_dir, fname)

        if idx < 6:
            pspec = PRESCRIPTION_SPECS[rx_indices[idx]]
            _, px_per_char = render_prescription_spec(pspec, fpath)
        else:
            _, px_per_char = render_photographic_benchmark_sample(
                spec, fpath, use_spec_font=True, font_size=21
            )
        logged_px_chars.append(px_per_char)

        # Copy original manifest entry exactly
        orig_entry = orig_test_manifest[idx]
        assert orig_entry["id"] == tid
        entry = dict(orig_entry)
        # Update filename / image path to point to spec directory
        entry["filename"] = fname
        entry["image_path"] = fpath
        manifest.append(entry)
        print(f"  [{idx+1:02d}/20] [{spec['category']:12s}] {spec['title']:36s} [px/char: {px_per_char:.2f}] -> {fpath}")

    manifest_path = os.path.join(output_dir, "test_manifest.json")
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

    with open(manifest_path, "rb") as f:
        m_sha = hashlib.sha256(f.read()).hexdigest()
    sha_path = os.path.join(output_dir, "test_manifest.sha256")
    with open(sha_path, "w") as f:
        f.write(f"{m_sha}  test_manifest.json\n")

    avg_px = sum(logged_px_chars) / len(logged_px_chars)
    print(f"\n[✓] Spec Test Set Successfully Compiled: {manifest_path}")
    print(f"    Manifest SHA256: {m_sha}")
    print(f"    Measured Average Resolution: {avg_px:.2f} px/char (Target: 12.8 +/- 1.0 px/char)\n")
    return manifest

if __name__ == "__main__":
    build_spec_testset()
