"""
PROJECT FRIDAY - VIZWIZ VALIDATION DATASET INGESTION & SUBSET FREEZE
Auditor Item C9a & C9b:
- Fetches official VizWiz validation annotations and images from vizwiz.cs.colorado.edu.
- Applies strict rule-based question filtering for text-reading tasks (C9b).
- Freezes a deterministic 500-sample subset (seed 42).
- Caches images locally (do NOT commit images).
- Persists signed subset.json manifest with image SHA256 hashes and metadata.
"""

import os
import sys
import io
import json
import random
import hashlib
import struct
import zlib
import time
import argparse
import urllib.request
import zipfile
import http.client
import requests
from requests.adapters import HTTPAdapter
import concurrent.futures
from typing import List, Dict, Any, Tuple
from PIL import Image

# Local repo imports
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(REPO_ROOT, "phase1_ai_sandbox/src"))
from eval_provenance import get_eval_provenance

ANNOTATIONS_URL = "https://vizwiz.cs.colorado.edu/VizWiz_final/vqa_data/Annotations.zip"
EXPECTED_ANNOTATIONS_SHA256 = "dbc32fc1e3f1b1039aea906030d569d6c238b4ddb2eea5e3453a6a565c829ec9"
IMAGES_ZIP_URL = "https://vizwiz.cs.colorado.edu/VizWiz_final/images/val.zip"
IMAGES_ZIP_TOTAL_BYTES = 3488913457
VIZWIZ_LICENSE = "Creative Commons Attribution 4.0 International License (CC BY 4.0)"
RANDOM_SEED = 42
SUBSET_TARGET_SIZE = 500

CACHE_DIR = os.path.join(REPO_ROOT, "phase1_ai_sandbox/external_train_data/vizwiz_cache")
IMAGES_CACHE_DIR = os.path.join(CACHE_DIR, "images")

# Selection Rule Definition Code for C9b
SELECTION_RULE_CODE = """def is_text_reading_question(q: str) -> bool:
    q_low = q.lower().strip()
    direct_patterns = [
        "what does this say",
        "what does it say",
        "what does the label",
        "what does this label",
        "what does the bottle",
        "what does the box",
        "what is written",
        "what is this written",
        "read",
        "expiration",
        "how much",
        "price",
        "dosage",
        "how many mg",
        "what kind of",
        "what flavor"
    ]
    for p in direct_patterns:
        if p in q_low:
            return True
    if "what is this" in q_low:
        targets = ["bottle", "box", "can", "label", "package", "medicine", "pill"]
        if any(t in q_low for t in targets):
            return True
    return False"""

exec(SELECTION_RULE_CODE, globals())

class RemoteZipReader(io.RawIOBase):
    def __init__(self, url: str, size: int):
        self.url = url
        self.size = size
        self.pos = 0

    def readable(self) -> bool: return True
    def seekable(self) -> bool: return True
    def seek(self, offset: int, whence: int = io.SEEK_SET) -> int:
        if whence == io.SEEK_SET: self.pos = offset
        elif whence == io.SEEK_CUR: self.pos += offset
        elif whence == io.SEEK_END: self.pos = self.size + offset
        return self.pos
    def tell(self) -> int: return self.pos
    def read(self, size: int = -1) -> bytes:
        if size == -1 or self.pos + size > self.size:
            size = self.size - self.pos
        if size <= 0: return b""
        req = urllib.request.Request(self.url, headers={"Range": f"bytes={self.pos}-{self.pos + size - 1}"})
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = resp.read()
        self.pos += len(data)
        return data

def fetch_annotations() -> List[Dict[str, Any]]:
    os.makedirs(CACHE_DIR, exist_ok=True)
    anno_cache_path = os.path.join(CACHE_DIR, "Annotations.zip")
    
    if os.path.exists(anno_cache_path):
        with open(anno_cache_path, "rb") as f:
            data = f.read()
        sha = hashlib.sha256(data).hexdigest()
        if sha == EXPECTED_ANNOTATIONS_SHA256:
            print(f"[✓] Using cached Annotations.zip ({len(data)} bytes, sha256={sha[:12]}...)")
        else:
            print(f"[*] Cache sha mismatch ({sha} != {EXPECTED_ANNOTATIONS_SHA256}). Re-downloading...")
            data = None
    else:
        data = None

    if data is None:
        print(f"[*] Downloading official VizWiz Annotations from: {ANNOTATIONS_URL}...")
        with urllib.request.urlopen(ANNOTATIONS_URL, timeout=30) as resp:
            data = resp.read()
        sha = hashlib.sha256(data).hexdigest()
        assert sha == EXPECTED_ANNOTATIONS_SHA256, f"Annotations sha256 mismatch! Expected {EXPECTED_ANNOTATIONS_SHA256}, got {sha}"
        with open(anno_cache_path, "wb") as f:
            f.write(data)
        print(f"[✓] Saved and verified Annotations.zip ({len(data)} bytes, sha256={sha[:12]}...)")

    z = zipfile.ZipFile(io.BytesIO(data))
    val_data = json.loads(z.read("val.json").decode("utf-8"))
    print(f"[✓] Extracted val.json with {len(val_data)} validation annotations.")
    return val_data

def select_subset(val_data: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    matching = [it for it in val_data if is_text_reading_question(it["question"])]
    matching_answerable = sum(1 for it in matching if it.get("answerable") == 1)
    matching_unanswerable = sum(1 for it in matching if it.get("answerable") == 0)
    print(f"[*] C9b Filter: {len(matching)} questions matched text-reading rule ({matching_answerable} answerable, {matching_unanswerable} unanswerable).")

    # Fixed seed random sample of SUBSET_TARGET_SIZE items
    rng = random.Random(RANDOM_SEED)
    if len(matching) > SUBSET_TARGET_SIZE:
        sampled = rng.sample(matching, SUBSET_TARGET_SIZE)
    else:
        sampled = list(matching)

    # Sort deterministically by image filename
    sampled = sorted(sampled, key=lambda x: x["image"])

    sample_answerable = sum(1 for it in sampled if it.get("answerable") == 1)
    sample_unanswerable = sum(1 for it in sampled if it.get("answerable") == 0)

    rule_sha256 = hashlib.sha256(SELECTION_RULE_CODE.encode("utf-8")).hexdigest()
    metadata = {
        "source_annotations_url": ANNOTATIONS_URL,
        "source_annotations_sha256": EXPECTED_ANNOTATIONS_SHA256,
        "source_images_url": IMAGES_ZIP_URL,
        "license": VIZWIZ_LICENSE,
        "total_val_annotations": len(val_data),
        "total_matching_rule": len(matching),
        "total_matching_answerable": matching_answerable,
        "total_matching_unanswerable": matching_unanswerable,
        "sampled_subset_size": len(sampled),
        "sampled_answerable": sample_answerable,
        "sampled_unanswerable": sample_unanswerable,
        "random_seed": RANDOM_SEED,
        "selection_rule_text": SELECTION_RULE_CODE,
        "selection_rule_sha256": rule_sha256
    }
    print(f"[✓] Frozen 500-item subset (seed {RANDOM_SEED}): {sample_answerable} answerable, {sample_unanswerable} unanswerable.")
    return sampled, metadata

def is_valid_jpeg(file_path: str) -> bool:
    try:
        with Image.open(file_path) as img:
            img.verify()
        return True
    except Exception:
        return False

def download_images(sampled_items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    os.makedirs(IMAGES_CACHE_DIR, exist_ok=True)
    needed = []
    manifest_items = []

    for it in sampled_items:
        img_name = it["image"]
        local_path = os.path.join(IMAGES_CACHE_DIR, img_name)
        if os.path.exists(local_path) and os.path.getsize(local_path) > 0 and is_valid_jpeg(local_path):
            with open(local_path, "rb") as f:
                img_bytes = f.read()
            img_sha = hashlib.sha256(img_bytes).hexdigest()
            manifest_items.append({
                "image": img_name,
                "sha256": img_sha,
                "question": it["question"],
                "answers": it["answers"],
                "answerable": it["answerable"],
                "answer_type": it.get("answer_type", "other")
            })
        else:
            if os.path.exists(local_path):
                try: os.remove(local_path)
                except OSError: pass
            needed.append(it)

    print(f"[*] Images status: {len(manifest_items)} already cached and valid, {len(needed)} to download.")

    if needed:
        print("[*] Mounting RemoteZipReader on vizwiz.cs.colorado.edu val.zip...")
        reader = RemoteZipReader(IMAGES_ZIP_URL, IMAGES_ZIP_TOTAL_BYTES)
        zf = zipfile.ZipFile(reader)
        info_map = {f.filename.replace("val/", ""): f for f in zf.filelist}

        session = requests.Session()
        adapter = HTTPAdapter(pool_connections=16, pool_maxsize=16, max_retries=3)
        session.mount("https://", adapter)
        session.mount("http://", adapter)

        def fetch_single_image(item: Dict[str, Any], max_retries: int = 5) -> Dict[str, Any]:
            img_name = item["image"]
            local_path = os.path.join(IMAGES_CACHE_DIR, img_name)
            if os.path.exists(local_path) and os.path.getsize(local_path) > 0 and is_valid_jpeg(local_path):
                with open(local_path, "rb") as f_in:
                    img_data = f_in.read()
            else:
                info = info_map[img_name]
                header_offset = info.header_offset
                csize = info.compress_size
                fetch_len = 30 + len(info.filename) + 128 + csize
                range_header = f"bytes={header_offset}-{header_offset + fetch_len - 1}"
                headers = {"Range": range_header}
                
                raw_chunk = None
                last_err = None
                for attempt in range(max_retries):
                    try:
                        resp = session.get(IMAGES_ZIP_URL, headers=headers, timeout=25)
                        if resp.status_code in (200, 206) and len(resp.content) >= 30:
                            raw_chunk = resp.content
                            break
                    except Exception as e:
                        last_err = e
                        time.sleep(0.5 * (attempt + 1))
                
                if raw_chunk is None or len(raw_chunk) < 30:
                    raise RuntimeError(f"Failed to fetch {img_name} after {max_retries} attempts: {last_err}")

                sig, ver, flag, meth, mtime, mdate, crc, csize_hdr, usize_hdr, fnlen, extralen = struct.unpack(
                    "<IHHHHHIIIHH", raw_chunk[:30]
                )
                data_start = 30 + fnlen + extralen
                comp_bytes = raw_chunk[data_start : data_start + csize_hdr]
                if meth == 8:
                    img_data = zlib.decompress(comp_bytes, -15)
                elif meth == 0:
                    img_data = comp_bytes
                else:
                    raise ValueError(f"Unsupported zip compression method {meth} for {img_name}")

                # Validate decompressed image bytes
                with Image.open(io.BytesIO(img_data)) as test_img:
                    test_img.verify()

                with open(local_path, "wb") as f_out:
                    f_out.write(img_data)

            img_sha = hashlib.sha256(img_data).hexdigest()
            return {
                "image": img_name,
                "sha256": img_sha,
                "question": item["question"],
                "answers": item["answers"],
                "answerable": item["answerable"],
                "answer_type": item.get("answer_type", "other")
            }

        num_workers = 16
        print(f"[*] Fetching {len(needed)} images using {num_workers} worker threads with persistent session pool...")
        completed = 0
        with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as ex:
            futures = {ex.submit(fetch_single_image, it): it for it in needed}
            for fut in concurrent.futures.as_completed(futures):
                manifest_items.append(fut.result())
                completed += 1
                if completed % 50 == 0 or completed == len(needed):
                    print(f"  [{completed}/{len(needed)}] images downloaded and verified.")

    # Sort manifest items deterministically by image name
    manifest_items = sorted(manifest_items, key=lambda x: x["image"])
    print(f"[✓] All {len(manifest_items)} subset images verified in local cache.")
    return manifest_items

def main():
    parser = argparse.ArgumentParser(description="Fetch and freeze VizWiz-VQA validation subset.")
    parser.add_argument("--allow-dirty", action="store_true", help="Allow uncommitted git working tree.")
    args = parser.parse_args()

    full_sha, short_sha, is_dirty, diff_hash = get_eval_provenance(REPO_ROOT, allow_dirty=args.allow_dirty)
    provenance = {
        "full_sha": full_sha,
        "short_sha": short_sha,
        "dirty": is_dirty,
        "diff_hash": diff_hash
    }
    print(f"[*] Provenance verified: commit {short_sha} (dirty={is_dirty})")

    output_dir = os.path.join(REPO_ROOT, f"phase1_ai_sandbox/eval_runs/{short_sha}/vizwiz_val")
    os.makedirs(output_dir, exist_ok=True)

    val_data = fetch_annotations()
    sampled_items, metadata = select_subset(val_data)
    manifest_items = download_images(sampled_items)

    manifest_payload = {
        "provenance": provenance,
        "metadata": metadata,
        "items": manifest_items
    }

    subset_path = os.path.join(output_dir, "subset.json")
    with open(subset_path, "w", encoding="utf-8") as f:
        json.dump(manifest_payload, f, indent=2)
    print(f"[✓] Saved frozen subset manifest ({len(manifest_items)} items) to: {subset_path}")

if __name__ == "__main__":
    main()
