"""
PROJECT FRIDAY - EXTRACTIVE LITERAL READER (Auditor Items B1-B4 & BR1-BR4)
Extracts verbatim optical facts from OCR lines with geometric alignment
and zero generative hallucination risk.
Author: Krishna Jagat Solanki
"""

import re

# Auditor Item B2 Constants & Dev Set Disclosure
# tuned on dev set: Minimum OCR line confidence threshold set to 0.60; dev set minimum is 0.7765 on hand-held angle captures; lines below 0.60 are rejected as optical noise to protect against hallucinations.
CONFIDENCE_THRESHOLD = 0.60

REFUSAL_TEXT = "I can't read that clearly. Please hold it closer."

# Medicine strength regex: drug-like word + optional salt + number + unit
STRENGTH_PAT = re.compile(
    r"\b([a-zA-Z]{3,})\s+(?:hcl\s+|sodium\s+|calcium\s+|besylate\s+|sulfate\s+|propionate\s+)?(\d+(?:\.\d+)?)\s*(mg|mcg|ml|g)\b",
    re.IGNORECASE
)

# BR3: Directions start verb: must START with the verb, not merely contain it
DIRECTIONS_START = re.compile(
    r"^\s*(?:[\d\.\-\*]\s*)*(take|use|apply|inhale|spray|insert|instill|inject|swallow|chew|give)\b",
    re.IGNORECASE
)

# BR3: Lines starting with warning words are never directions
WARNING_START = re.compile(
    r"^\s*(do\s+not|don'?t|never|avoid|warning|caution|for\s+external|keep)\b",
    re.IGNORECASE
)

# BR2: Stop prefix for following directions lines (new fields or warnings)
STOP_FIELD_PREFIXES = re.compile(
    r"^\s*(qty|quantity|refill|exp|date|discard|rx|dr\.?|prescriber|patient|pharmacy|store|call|m[rs]\.?|wa\b|war\b|warn\b|warning|caution|keep|avoid|do\s+not|don'?t|never|for\s+external|may\s+cause)\b",
    re.IGNORECASE
)

# BR2: Frequency and interval expressions
FREQ_PATTERN = re.compile(
    r"\b(daily|twice|once|thrice|\d+\s*times|times\s+daily|every\s+\d+|every\s+other\s+day|weekly|monthly|hourly|at\s+bedtime|before\s+breakfast|with\s+meals|as\s+needed|prn|in\s+the\s+morning|in\s+the\s+evening|at\s+night)\b",
    re.IGNORECASE
)

# Question stopwords
STOPWORDS = {
    "what", "is", "the", "on", "this", "in", "for", "how", "much", "does",
    "cost", "which", "according", "to", "state", "show", "shown", "stated",
    "indicated", "marked", "reported", "achieve", "house", "when", "where",
    "who", "a", "an", "do", "does", "are", "by", "of", "and", "or", "at",
    "from", "with", "that", "it", "its", "you", "your", "can", "could", "all",
    "please", "tell", "me", "text", "image", "photo", "document", "picture", "sign", "label",
    "was", "were", "be", "been", "being"
}

# Generic price and field words (not specific to an entity)
GENERIC_FIELD_WORDS = {
    "price", "cost", "how", "much", "rate", "fee", "amount", "due", "total", "charge",
    "charges", "charged", "check", "value", "ceiling", "maximum", "max", "minimum", "min",
    "setting", "level", "average", "rules", "rule", "conduct", "topic", "classification",
    "notice", "plaque", "display", "cabinet", "window", "bill", "receipt", "invoice", "insert",
    "counter", "bench", "area", "menu", "final", "net", "gross", "current", "allowed",
    "number", "numbers", "time", "date", "hours", "per", "kwh", "summary", "status",
    "parking", "charging", "rental", "car", "table", "room", "grocery", "electric",
    "kilowatt", "hour"
}

def clean_alphanumeric(s: str) -> str:
    """Removes non-alphanumeric characters and converts to lowercase."""
    return re.sub(r"[^a-z0-9]", "", str(s).lower())

def is_dirty_value_token(text: str) -> tuple[bool, str]:
    """
    BR1 (b): A spoken price/number must be a clean token.
    Refuse if a letter is glued to a currency/number (e.g. 'B$4.75', '$4.75B'),
    or the currency symbol is separated from digits by letters.
    """
    # 1. Letter glued before currency symbol: e.g. B$4.75
    if re.search(r"[a-zA-Z]+[\$£€¥₹]", text):
        return True, "Letter glued before currency symbol"
    # 2. Letter glued immediately after currency symbol before digit: e.g. $B4.75
    if re.search(r"[\$£€¥₹][a-zA-Z]+", text):
        return True, "Letter glued immediately after currency symbol"
    # 3. Letter glued to numeric value in currency token: e.g. $4.75B
    if re.search(r"[\$£€¥₹]\s*\d+(?:\.\d+)?[a-zA-Z]+", text):
        return True, "Letter glued to numeric value in currency token"
    # 4. Currency symbol separated from digits by letters: e.g. $ abc 4.75
    if re.search(r"[\$£€¥₹]\s+[a-zA-Z]+\s+\d+", text):
        return True, "Currency symbol separated from digits by letters"
    return False, ""

def boxes_y_overlap(box1: list, box2: list, threshold: float = 0.5) -> bool:
    """
    Auditor Item B2: Checks if two bounding boxes vertically overlap on the same row.
    box format: [[x0, y0], [x1, y1], [x2, y2], [x3, y3]]
    """
    if not box1 or not box2:
        return False
    try:
        y1_min = min(pt[1] for pt in box1)
        y1_max = max(pt[1] for pt in box1)
        y2_min = min(pt[1] for pt in box2)
        y2_max = max(pt[1] for pt in box2)
    except Exception:
        return False

    inter = max(0.0, min(y1_max, y2_max) - max(y1_min, y2_min))
    h1 = max(1.0, y1_max - y1_min)
    h2 = max(1.0, y2_max - y2_min)
    return (inter / min(h1, h2)) >= threshold

def is_same_row(box1: list, box2: list) -> bool:
    """
    Checks if box2 is in the same row as box1 (with potential vertical offset).
    Handles typography baseline offset, camera perspective, and separate bounding boxes.
    """
    if not box1 or not box2:
        return False
    try:
        y1_min = min(pt[1] for pt in box1)
        y1_max = max(pt[1] for pt in box1)
        y2_min = min(pt[1] for pt in box2)
        y2_max = max(pt[1] for pt in box2)
        h1 = max(1.0, y1_max - y1_min)
        h2 = max(1.0, y2_max - y2_min)
        mid1 = (y1_min + y1_max) / 2.0
        mid2 = (y2_min + y2_max) / 2.0
        inter = max(0.0, min(y1_max, y2_max) - max(y1_min, y2_min))
        overlap = inter / min(h1, h2)
        center_dist = abs(mid1 - mid2)
        return (overlap >= 0.20) or (center_dist <= max(h1, h2) * 0.75 and center_dist <= 30.0)
    except Exception:
        return False

SECONDARY_FIELD_INDICATORS = {
    "password", "wifi", "network", "hours", "time", "arrival", "arriving",
    "gate", "flight", "destination", "location", "located",
    "floor", "floors", "elevator", "rule", "rules", "conduct",
    "topic", "status", "setting", "classification", "class", "value"
}

SPLIT_PAT = re.compile(
    r"\band\b|\+|\bfor\b|\bshown on\b|\bposted on\b|\bscheduled on\b|\bindicated (?:at|on)\b|\baccording to\b|\bon this\b|\bwhere\b|\bwhen\b",
    re.I
)

def validate_line(line: dict, line_id: int) -> tuple[bool, str | None]:
    """
    Auditor Item B2 Validation:
    Refuse if confidence < threshold, or normalization_changed on digit line,
    or ambiguous numeral detected.
    """
    conf = float(line.get("confidence", 1.0))
    raw_t = str(line.get("raw_text", ""))

    # 1. Confidence threshold
    if conf < CONFIDENCE_THRESHOLD:
        return False, f"Line {line_id} confidence {conf:.2f} below threshold {CONFIDENCE_THRESHOLD}"

    # 2. Normalization changed on line with digit
    if line.get("normalization_changed", False) and any(c.isdigit() for c in raw_t):
        return False, f"Ambiguous numeral substitution detected on line {line_id} with digits"

    # 3. Ambiguous-numeral check: OCR confusion patterns (e.g. 'O' followed by digit or digit followed by 'O')
    if re.search(r"\b[Oo]\d+|\d+[Oo]\b", raw_t):
        return False, f"Ambiguous numeral pattern detected on line {line_id}: '{raw_t}'"

    return True, None

def read_literal(ocr_lines: list, category: str, question: str) -> dict:
    """
    Auditor Item B2 & BR1-BR4: Single entry point for Extractive Literal Reader.
    Signature: read_literal(ocr_lines, category, question) ->
        {"speech": str, "source_line_ids": list[int], "refusal_reason": str | None}
    """
    if not ocr_lines:
        return {
            "speech": REFUSAL_TEXT,
            "source_line_ids": [],
            "refusal_reason": "No text detected in OCR"
        }

    cat = (category or "").lower()
    q_lower = (question or "").lower()

    # -------------------------------------------------------------
    # 1. MEDICINE CATEGORY (BR2, BR3, BR4)
    # -------------------------------------------------------------
    if cat == "medicine" or any(w in q_lower for w in ["medication", "prescribed dose", "prescription"]):
        # BR4: Count STRENGTH_PAT matches across all lines
        strength_matches = []
        for i, line in enumerate(ocr_lines):
            t = str(line.get("raw_text", ""))
            m = STRENGTH_PAT.search(t)
            if m:
                drug_norm = m.group(1).lower()
                dose_norm = f"{m.group(2)}{m.group(3).lower()}"
                strength_matches.append((i, drug_norm, dose_norm))

        if not strength_matches:
            return {
                "speech": REFUSAL_TEXT,
                "source_line_ids": [],
                "refusal_reason": "No valid drug strength line found on label"
            }

        # BR4: If >1 distinct drug-strength -> refuse
        distinct_strengths = set((m[1], m[2]) for m in strength_matches)
        if len(distinct_strengths) > 1:
            return {
                "speech": REFUSAL_TEXT,
                "source_line_ids": [m[0] for m in strength_matches],
                "refusal_reason": f"Multiple distinct drug strength lines found on label ({len(distinct_strengths)} distinct strengths); ambiguous target"
            }

        str_idx = strength_matches[0][0]
        str_box = ocr_lines[str_idx].get("box", [])
        str_ymax = max(pt[1] for pt in str_box) if str_box else 0

        # BR3: Find directions start line: must START with the verb; warning lines are excluded
        dir_start_candidates = []
        for i in range(len(ocr_lines)):
            if i == str_idx:
                continue
            line = ocr_lines[i]
            t = str(line.get("raw_text", ""))
            b = line.get("box", [])
            b_ymin = min(pt[1] for pt in b) if b else 0

            # Must be below strength line
            is_below = (b_ymin >= str_ymax - 5) if (str_box and b) else (i > str_idx)
            if not is_below:
                continue

            # BR3: Warning lines are NEVER directions
            if WARNING_START.search(t):
                continue

            # BR3: Must START with verb
            if DIRECTIONS_START.search(t):
                dist = b_ymin - str_ymax if (str_box and b) else (i - str_idx) * 10
                dir_start_candidates.append((dist, i))

        if not dir_start_candidates:
            return {
                "speech": REFUSAL_TEXT,
                "source_line_ids": [str_idx],
                "refusal_reason": "Prescription directions line missing below strength line"
            }

        # BR3: If more than one dosing block exists (quantity + frequency) -> refuse
        dosing_blocks = []
        for _, c_idx in dir_start_candidates:
            c_text = str(ocr_lines[c_idx].get("raw_text", ""))
            has_qty = bool(re.search(r"\b(?:\d+|(?:one|two|three|four))\s*(?:tablet|tablets|capsule|capsules|puff|puffs|spray|sprays|drop|drops|ml|mg)\b", c_text, re.I))
            has_freq = bool(FREQ_PATTERN.search(c_text))
            if has_qty and has_freq:
                dosing_blocks.append(c_idx)

        if len(dosing_blocks) > 1:
            return {
                "speech": REFUSAL_TEXT,
                "source_line_ids": dosing_blocks,
                "refusal_reason": f"Multiple dosing blocks ({len(dosing_blocks)}) detected on label; ambiguous directions"
            }

        dir_start_candidates.sort(key=lambda x: x[0])
        dir_start_idx = dir_start_candidates[0][1]

        # BR2: Assemble the directions block: directions start line PLUS following lines
        dir_block_ids = [dir_start_idx]
        prev_idx = dir_start_idx

        for j in range(dir_start_idx + 1, len(ocr_lines)):
            line_j = ocr_lines[j]
            t_j = str(line_j.get("raw_text", "")).strip()
            b_j = line_j.get("box", [])

            # Check if line j is a new field header or warning
            if STOP_FIELD_PREFIXES.search(t_j):
                break

            # Geometry check: vertical gap
            b_prev = ocr_lines[prev_idx].get("box", [])
            if b_prev and b_j:
                try:
                    y0_prev = min(pt[1] for pt in b_prev)
                    y1_prev = max(pt[1] for pt in b_prev)
                    h_prev = max(1.0, y1_prev - y0_prev)
                    y0_j = min(pt[1] for pt in b_j)
                    y1_j = max(pt[1] for pt in b_j)

                    gap = y0_j - y1_prev
                    if gap > 2.5 * h_prev:
                        # Large vertical gap -> directions block ended
                        break
                    if y0_j < y0_prev - 10:
                        # Above previous line -> not following
                        break
                except Exception:
                    pass

            dir_block_ids.append(j)
            prev_idx = j

        # Validate all lines in medicine response
        all_med_line_ids = [str_idx] + dir_block_ids
        for l_idx in all_med_line_ids:
            is_valid, reason = validate_line(ocr_lines[l_idx], l_idx)
            if not is_valid:
                return {
                    "speech": REFUSAL_TEXT,
                    "source_line_ids": all_med_line_ids,
                    "refusal_reason": reason
                }

        # Build directions block text
        dir_parts = [str(ocr_lines[idx].get("raw_text", "")).strip().rstrip(".") for idx in dir_block_ids]
        dir_block_text = " ".join(dir_parts).strip()

        # BR2: If the directions block contains no frequency/interval expression -> refuse
        if not FREQ_PATTERN.search(dir_block_text):
            return {
                "speech": REFUSAL_TEXT,
                "source_line_ids": all_med_line_ids,
                "refusal_reason": "Directions block missing frequency or interval expression"
            }

        str_text = str(ocr_lines[str_idx].get("raw_text", "")).strip().rstrip(".")
        speech = f"{str_text}. {dir_block_text}."
        return {
            "speech": speech,
            "source_line_ids": all_med_line_ids,
            "refusal_reason": None
        }

    # -------------------------------------------------------------
    # 2. GENERAL / MENU / SIGNAGE / DOCUMENT / SCENE_TEXT
    # -------------------------------------------------------------
    clauses = [p.strip() for p in SPLIT_PAT.split(q_lower) if p.strip()]
    if not clauses:
        clauses = [q_lower]
    target_line_ids = []

    for clause in clauses:
        c_words = [w for w in re.findall(r"[a-z0-9]+", clause) if w not in STOPWORDS and len(w) >= 2]
        if not c_words:
            continue
        is_price_clause = any(w in c_words for w in ["price", "cost", "how", "much", "rate", "total", "charged", "fee", "amount", "due", "check", "pay", "payable"])
        entity_content_words = [w for w in c_words if w not in GENERIC_FIELD_WORDS]

        # If a clause has NO entity content words (only generic words like "sign", "menu", "counter", "window", "cabinet"), skip it
        if not entity_content_words and not is_price_clause:
            continue

        scored_lines = []
        for i, line in enumerate(ocr_lines):
            t_raw = str(line.get("raw_text", ""))
            t_low = t_raw.lower()
            line_tokens = set(re.findall(r"[a-z0-9]+", t_low))
            matches = 0
            for w in c_words:
                if len(w) <= 2:
                    if w in line_tokens:
                        matches += 1
                else:
                    if (w in line_tokens) or (w in t_low) or any((t.startswith(w) or w.startswith(t)) and len(min(w, t, key=len)) >= 3 for t in line_tokens):
                        matches += 1
            if matches == 0:
                continue
            has_price = bool(re.search(r"[\$£€¥₹]\s*\d+|\d+\s*[\$£€¥₹]|\busd\b", t_low))
            has_label_val = (":" in t_raw) or ("-" in t_raw and any(c.isdigit() for c in t_raw))
            has_sec = any(sw in t_low for sw in SECONDARY_FIELD_INDICATORS if sw in c_words)
            score = matches * 2
            if is_price_clause and has_price:
                score += 3
            if has_label_val:
                score += 2
            if has_sec:
                score += 2
            scored_lines.append((score, matches, i, line))

        if not scored_lines:
            if is_price_clause and entity_content_words:
                return {"speech": REFUSAL_TEXT, "source_line_ids": [], "refusal_reason": f"Queried entity words {entity_content_words} not found on menu/sign"}
            continue

        # Sort primarily by score, secondarily by number of distinct matched query words
        scored_lines.sort(key=lambda x: (x[0], x[1]), reverse=True)
        top_score, top_matches, top_idx, top_line = scored_lines[0]
        if is_price_clause and entity_content_words:
            top_tokens = set(re.findall(r"[a-z0-9]+", top_line.get("raw_text", "").lower()))
            top_raw_low = top_line.get("raw_text", "").lower()
            for ew in entity_content_words:
                matched = (ew in top_tokens) if len(ew) <= 2 else ((ew in top_tokens) or (ew in top_raw_low))
                if not matched:
                    return {"speech": REFUSAL_TEXT, "source_line_ids": [top_idx], "refusal_reason": f"Entity content word '{ew}' missing or corrupted in candidate line"}

        if len(scored_lines) > 1 and scored_lines[1][0] == top_score and scored_lines[1][1] == top_matches:
            b1 = top_line.get("box", [])
            b2 = scored_lines[1][3].get("box", [])
            if b1 and b2 and is_same_row(b1, b2):
                idx2 = scored_lines[1][2]
                if top_idx not in target_line_ids:
                    target_line_ids.append(top_idx)
                if idx2 not in target_line_ids:
                    target_line_ids.append(idx2)
            else:
                l1_tokens = set(re.findall(r"[a-z0-9]+", top_line.get("raw_text", "").lower()))
                l2_tokens = set(re.findall(r"[a-z0-9]+", scored_lines[1][3].get("raw_text", "").lower()))
                words_l1 = {w for w in c_words if w in l1_tokens}
                words_l2 = {w for w in c_words if w in l2_tokens}
                if words_l1 and words_l2 and len(words_l1 & words_l2) == 0:
                    if top_idx not in target_line_ids:
                        target_line_ids.append(top_idx)
                    if scored_lines[1][2] not in target_line_ids:
                        target_line_ids.append(scored_lines[1][2])
                else:
                    l1_has_val = (":" in top_line.get("raw_text", "")) or bool(re.search(r"\d", top_line.get("raw_text", "")))
                    l2_has_val = (":" in scored_lines[1][3].get("raw_text", "")) or bool(re.search(r"\d", scored_lines[1][3].get("raw_text", "")))
                    if l1_has_val and not l2_has_val:
                        if top_idx not in target_line_ids:
                            target_line_ids.append(top_idx)
                    elif l2_has_val and not l1_has_val:
                        if scored_lines[1][2] not in target_line_ids:
                            target_line_ids.append(scored_lines[1][2])
                    else:
                        return {"speech": REFUSAL_TEXT, "source_line_ids": [top_idx, scored_lines[1][2]], "refusal_reason": "Candidate query match is not unique"}
        else:
            if top_idx not in target_line_ids:
                target_line_ids.append(top_idx)

    if not target_line_ids:
        q_words = [w for w in re.findall(r"[a-z0-9]+", q_lower) if w not in STOPWORDS and len(w) >= 2]
        scored_lines = []
        for i, line in enumerate(ocr_lines):
            t_raw = str(line.get("raw_text", ""))
            t_low = t_raw.lower()
            line_tokens = set(re.findall(r"[a-z0-9]+", t_low))
            matches = sum(1 for w in q_words if (w in line_tokens) or (len(w) >= 3 and any(t.startswith(w) or t.endswith(w) for t in line_tokens)))
            if matches > 0:
                scored_lines.append((matches, i, line))
        if scored_lines:
            scored_lines.sort(key=lambda x: x[0], reverse=True)
            target_line_ids.append(scored_lines[0][1])

    if not target_line_ids:
        return {"speech": REFUSAL_TEXT, "source_line_ids": [], "refusal_reason": "No relevant OCR line matching query found"}

    target_line_ids = sorted(list(set(target_line_ids)))

    # Rule 1: Associate row-aligned price box on same row (with potential vertical offset)
    is_price_q = any(w in q_lower for w in ["price", "cost", "how much", "rate", "total", "charged", "fee", "amount", "due", "pay", "payable"])
    if is_price_q:
        current_has_price = any(bool(re.search(r"[\$£€¥₹]\s*\d+|\d+\s*[\$£€¥₹]|\b\d+\.\d{2}\b", str(ocr_lines[k].get("raw_text", "")))) for k in target_line_ids)
        if not current_has_price:
            for tid in list(target_line_ids):
                b_item = ocr_lines[tid].get("box", [])
                candidates = []
                for j, o_line in enumerate(ocr_lines):
                    if j in target_line_ids:
                        continue
                    raw_j = str(o_line.get("raw_text", ""))
                    if not re.search(r"[\$£€¥₹]\s*\d+|\d+\s*[\$£€¥₹]|\b\d+\.\d{2}\b", raw_j):
                        continue
                    b_j = o_line.get("box", [])
                    if b_item and b_j and is_same_row(b_item, b_j):
                        x_item_max = max(pt[0] for pt in b_item)
                        x_j_min = min(pt[0] for pt in b_j)
                        dist = abs(x_j_min - x_item_max)
                        candidates.append((dist, j))
                if candidates:
                    candidates.sort(key=lambda x: x[0])
                    target_line_ids.append(candidates[0][1])
                    target_line_ids.sort()
                    break

    # Rule 2: Multi-field secondary key field extraction (e.g. gate + time, status, wifi password, hours)
    q_sec_words = [sw for sw in SECONDARY_FIELD_INDICATORS if sw in q_lower]
    if q_sec_words:
        selected_texts = " ".join([str(ocr_lines[k].get("raw_text", "")).lower() for k in target_line_ids])
        missing_sec = [sw for sw in q_sec_words if sw not in selected_texts]
        if missing_sec:
            for j, o_line in enumerate(ocr_lines):
                if j in target_line_ids:
                    continue
                raw_j = str(o_line.get("raw_text", ""))
                low_j = raw_j.lower()
                has_missing = any(sw in low_j for sw in missing_sec)
                # If question asked for rules or conduct, match prohibition/conduct phrasing on sign
                if not has_missing and any(sw in ("rules", "rule", "conduct") for sw in missing_sec):
                    has_missing = bool(re.search(r"\b(?:no|do not|please|silent|quiet|prohibited)\b", low_j))
                has_label_val = (":" in raw_j) or bool(re.search(r"\d", raw_j)) or ("-" in raw_j)
                if has_missing and has_label_val:
                    target_line_ids.append(j)
                    target_line_ids.sort()
                    break

    for l_idx in target_line_ids:
        is_valid, reason = validate_line(ocr_lines[l_idx], l_idx)
        if not is_valid:
            return {"speech": REFUSAL_TEXT, "source_line_ids": target_line_ids, "refusal_reason": reason}
        raw_t = str(ocr_lines[l_idx].get("raw_text", ""))
        is_dirty, dirty_reason = is_dirty_value_token(raw_t)
        if is_dirty:
            return {"speech": REFUSAL_TEXT, "source_line_ids": target_line_ids, "refusal_reason": dirty_reason}

    spoken_parts = [str(ocr_lines[k].get("raw_text", "")).strip().rstrip(".") for k in target_line_ids]
    speech = ". ".join(spoken_parts)
    if speech and not speech.endswith("."):
        speech += "."

    # Rule 3: VizWiz V1 Refusals
    # 3a. For price questions, refuse if no numeric price token is spoken
    if is_price_q:
        has_numeric_price = bool(re.search(r"[\$£€¥₹]\s*\d+|\d+\s*[\$£€¥₹]|\b\d+\.\d{2}\b", speech))
        if not has_numeric_price:
            return {"speech": REFUSAL_TEXT, "source_line_ids": target_line_ids, "refusal_reason": "Price requested but no price token found in selected text (VizWiz V1)"}

    # 3b. Refuse when selected line adds no tokens beyond question words (VizWiz V1 echo refusal)
    q_tokens = set(re.findall(r"[a-z0-9]+", q_lower))
    s_tokens = set(re.findall(r"[a-z0-9]+", speech.lower()))
    carrier_words = STOPWORDS | GENERIC_FIELD_WORDS | {"the", "a", "an", "is", "are", "on", "in", "at", "to", "for", "of", "and", "or", "what", "which", "when", "where", "how", "this", "that", "storage", "room", "center"}
    informative_tokens = {t for t in s_tokens if t not in q_tokens and t not in carrier_words}
    if len(informative_tokens) == 0:
        # Check if adjacent following line contains the requested attribute/value (e.g. room number, code, value)
        max_tid = max(target_line_ids)
        if max_tid + 1 < len(ocr_lines):
            next_line = ocr_lines[max_tid + 1]
            raw_next = str(next_line.get("raw_text", "")).strip()
            # If next line has digits or specific value identifier (e.g. Room 301, Suite 2B, Gate 4)
            if re.search(r"\b\d+\b", raw_next) or re.search(r"\b(?:room|suite|gate|dept|no|fl)\b", raw_next.lower()):
                is_valid, _ = validate_line(next_line, max_tid + 1)
                is_dirty, _ = is_dirty_value_token(raw_next)
                if is_valid and not is_dirty:
                    target_line_ids.append(max_tid + 1)
                    target_line_ids.sort()
                    spoken_parts = [str(ocr_lines[k].get("raw_text", "")).strip().rstrip(".") for k in target_line_ids]
                    speech = ". ".join(spoken_parts) + "."
                    s_tokens = set(re.findall(r"[a-z0-9]+", speech.lower()))
                    informative_tokens = {t for t in s_tokens if t not in q_tokens and t not in carrier_words}

        if len(informative_tokens) == 0:
            return {"speech": REFUSAL_TEXT, "source_line_ids": target_line_ids, "refusal_reason": "Selected line adds no tokens beyond question words (VizWiz V1 echo refusal)"}

    return {"speech": speech, "source_line_ids": target_line_ids, "refusal_reason": None}


def run_literal_reader_unit_tests():
    """
    BR5: Unit tests on synthetic OCRLine lists with boxes (CPU).
    Covers the 3 BR probes + 4 additional edge case probes.
    """
    try:
        from benchmark_dataset_evaluator import OCRLine
    except ImportError:
        try:
            from phase1_ai_sandbox.src.benchmark_dataset_evaluator import OCRLine
        except ImportError:
            OCRLine = globals().get("OCRLine")

    def make_line(text: str, y0: float = 0, y1: float = 20, conf: float = 0.95):
        return OCRLine(
            raw_text=text,
            normalized_text=text,
            normalization_changed=False,
            box=[[10, y0], [200, y0], [200, y1], [10, y1]],
            confidence=conf,
            reading_order=0
        )

    # 1. BR2 probe: Wrapped directions drop frequency
    # "WARFARIN 5 MG TABLET", "TAKE 1 TABLET BY MOUTH", "EVERY OTHER DAY" -> speech contains "EVERY OTHER DAY"
    lines1 = [
        make_line("WARFARIN 5 MG TABLET", 10, 30),
        make_line("TAKE 1 TABLET BY MOUTH", 40, 60),
        make_line("EVERY OTHER DAY", 65, 85),
    ]
    res1 = read_literal(lines1, "medicine", "What medication is this and what is the prescribed dose?")
    assert "EVERY OTHER DAY" in res1["speech"], f"Probe 1 failed: {res1}"

    # 2. BR3 probe: Warning line chosen as directions
    # "METHOTREXATE 2.5 MG TABLET", "DO NOT TAKE WITH ALCOHOL", "TAKE 4 TABLETS ONCE WEEKLY"
    # -> speech contains "TAKE 4 TABLETS ONCE WEEKLY" and NOT "ALCOHOL"
    lines2 = [
        make_line("METHOTREXATE 2.5 MG TABLET", 10, 30),
        make_line("DO NOT TAKE WITH ALCOHOL", 35, 55),
        make_line("TAKE 4 TABLETS ONCE WEEKLY", 60, 80),
    ]
    res2 = read_literal(lines2, "medicine", "What medication is this and what is the prescribed dose?")
    assert "TAKE 4 TABLETS ONCE WEEKLY" in res2["speech"], f"Probe 2 failed: {res2}"
    assert "ALCOHOL" not in res2["speech"], f"Probe 2 failed (included warning): {res2}"

    # 3. BR4 probe: Multiple strength lines (two-drug probe)
    # "IBUPROFEN 200 MG", "ACETAMINOPHEN 500 MG TABLET", "TAKE 2 TABLETS EVERY 6 HOURS" -> REFUSAL_TEXT
    lines3 = [
        make_line("IBUPROFEN 200 MG", 10, 30),
        make_line("ACETAMINOPHEN 500 MG TABLET", 35, 55),
        make_line("TAKE 2 TABLETS EVERY 6 HOURS", 60, 80),
    ]
    res3 = read_literal(lines3, "medicine", "What medication is this and what is the prescribed dose?")
    assert res3["speech"] == REFUSAL_TEXT, f"Probe 3 failed: {res3}"

    # 4. BR2 probe: Directions with no frequency
    # "WARFARIN 5 MG TABLET", "TAKE 1 TABLET BY MOUTH" only -> REFUSAL_TEXT
    lines4 = [
        make_line("WARFARIN 5 MG TABLET", 10, 30),
        make_line("TAKE 1 TABLET BY MOUTH", 40, 60),
    ]
    res4 = read_literal(lines4, "medicine", "What medication is this and what is the prescribed dose?")
    assert res4["speech"] == REFUSAL_TEXT, f"Probe 4 failed: {res4}"

    # 5. BR1 probe: Menu ambiguity - candidate not unique
    # "ICED LATTE $5.00" / "OAT MILK LATTE $5.50", Q "price of the latte" -> REFUSAL_TEXT (not unique)
    lines5 = [
        make_line("ICED LATTE $5.00", 10, 30),
        make_line("OAT MILK LATTE $5.50", 40, 60),
    ]
    res5 = read_literal(lines5, "signage_menu", "What is the price of the latte?")
    assert res5["speech"] == REFUSAL_TEXT, f"Probe 5 failed: {res5}"
    assert "unique" in (res5["refusal_reason"] or "").lower(), f"Probe 5 unexpected reason: {res5}"

    # 6. BR1 probe: Menu with item missing -> REFUSAL_TEXT
    lines6 = [
        make_line("ICED LATTE $5.00", 10, 30),
        make_line("OAT MILK LATTE $5.50", 40, 60),
    ]
    res6 = read_literal(lines6, "signage_menu", "What is the price of Matcha Latte on this menu?")
    assert res6["speech"] == REFUSAL_TEXT, f"Probe 6 failed: {res6}"

    # 7. BR1 probe: "COLD EW.... B$4.75" for Q "Cold Brew" -> REFUSAL_TEXT via BR1 general rules
    lines7 = [
        make_line("ARTISAN COFFEE ROASTERS", 10, 30),
        make_line("COLD EW.... B$4.75", 40, 60),
        make_line("OAT MILK LATTE $5.50", 70, 90),
    ]
    res7 = read_literal(lines7, "signage_menu", "What is the price of Cold Brew on this menu?")
    assert res7["speech"] == REFUSAL_TEXT, f"Probe 7 failed: {res7}"

    # 8. Round D probe: Price in separate vertically offset box on same row (y-overlap or row alignment)
    def make_boxed_line(text: str, y0: float, y1: float, x0: float, x1: float, conf: float = 0.95):
        return OCRLine(
            raw_text=text,
            normalized_text=text,
            normalization_changed=False,
            box=[[x0, y0], [x1, y0], [x1, y1], [x0, y1]],
            confidence=conf,
            reading_order=0
        )
    lines8 = [
        make_boxed_line("COLD BREW", y0=100, y1=120, x0=40, x1=120),
        make_boxed_line("$4.75", y0=108, y1=128, x0=180, x1=230)
    ]
    res8 = read_literal(lines8, "signage_menu", "What is the price of Cold Brew on this menu?")
    assert "$4.75" in res8["speech"] and "COLD BREW" in res8["speech"], f"Probe 8 failed: {res8}"

    # 9. Round D probe: Multi-field scene/sign answers (secondary key field extraction)
    lines9 = [
        make_line("GATE B24-ON TIME", 50, 70),
        make_line("FLIGHT AI 102 -> LONDON HEATHROW", 80, 100)
    ]
    res9 = read_literal(lines9, "signage_menu", "What is the departure gate and flight number?")
    assert "GATE B24" in res9["speech"] and "FLIGHT AI 102" in res9["speech"], f"Probe 9 failed: {res9}"

    # 10. Round D probe: VizWiz V1 echo refusal (selected line adds no tokens beyond question words)
    lines10 = [
        make_line("NO PARKING", 50, 70)
    ]
    res10 = read_literal(lines10, "scene_text", "Does this sign say no parking?")
    assert res10["speech"] == REFUSAL_TEXT, f"Probe 10 failed: {res10}"
    assert "VizWiz V1" in (res10["refusal_reason"] or ""), f"Probe 10 unexpected reason: {res10}"

    # 11. Round D probe: VizWiz V1 price question without price token
    lines11 = [
        make_line("COLD BREW", 50, 70)
    ]
    res11 = read_literal(lines11, "signage_menu", "What is the price of Cold Brew?")
    assert res11["speech"] == REFUSAL_TEXT, f"Probe 11 failed: {res11}"
    assert "price" in (res11["refusal_reason"] or "").lower(), f"Probe 11 unexpected reason: {res11}"

    # 12. Round F probe: Directory / list adjacent value line association (Rule A)
    # When selected line is an entity label with no digits, and following line has the requested number/value
    lines12 = [
        make_line("NEUROLOGY CLINIC", 50, 70),
        make_line("ROOM 402", 75, 95),
        make_line("CARDIOLOGY WING", 100, 120),
        make_line("ROOM 408", 125, 145)
    ]
    res12 = read_literal(lines12, "signage_menu", "Which room number is the Neurology Clinic?")
    assert "NEUROLOGY CLINIC" in res12["speech"] and "ROOM 402" in res12["speech"], f"Probe 12 failed: {res12}"
    assert "CARDIOLOGY" not in res12["speech"], f"Probe 12 included wrong wing: {res12}"

    # 13. Round F probe: Conduct rules line association (Rule B)
    # When question queries conduct/rules and top match is facility header, associate rule/prohibition line
    lines13 = [
        make_line("CAMPUS SCIENCE LIBRARY - FLOOR 3", 40, 60),
        make_line("QUIET STUDY ZONE - NO CELL PHONES", 65, 85),
        make_line("INFORMATION DESK AT ENTRANCE", 90, 110)
    ]
    res13 = read_literal(lines13, "scene_text", "What are the conduct rules for this library floor?")
    assert "NO CELL PHONES" in res13["speech"], f"Probe 13 failed: {res13}"

    print("[✓] ALL 13 BR1-BR5 & ROUND D/F LITERAL READER UNIT TESTS PASSED!")

if __name__ == "__main__":
    run_literal_reader_unit_tests()
