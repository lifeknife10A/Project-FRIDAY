"""
PROJECT FRIDAY: REALISTIC HIGH-FIDELITY PRESCRIPTION LABEL BENCHMARK BUILDER
Generates 20 distinct high-resolution realistic pharmacy prescription labels
with complete hand-typed ground truth text and target clinical extractions.
NOTE: All pharmacy names are strictly fictional (anti-trademark / audit compliance).
"""

import os
import json
from PIL import Image, ImageDraw, ImageFont

PRESCRIPTION_SPECS = [
    {
        "pharmacy": "METROPOLIS APOTHECARY #101 - (555) 019-2834",
        "pharm_address": "1042 MAIN ST, NEW YORK, NY 10001",
        "rx_num": "RX # 6543210-0987",
        "date": "11/20/2026",
        "patient": "PATIENT: ELEANOR RIGBY",
        "doctor": "DR: DR. ROBERT HENDERSON, MD",
        "drug_line": "AMOXICILLIN 500 MG CAPSULE",
        "directions": "TAKE 1 CAPSULE BY MOUTH TWICE DAILY WITH MEALS FOR 10 DAYS",
        "warning": "WARNING: FINISH ALL MEDICATION UNLESS ADVISED BY DOCTOR",
        "qty_refills": "QTY: 20 CAPSULES   REFILLS: 0   EXP: 11/2027",
        "ndc_mfr": "NDC: 0093-2264-01   TEVA PHARMACEUTICALS",
        "target_drug_dose": "Amoxicillin 500mg",
        "footer": "KEEP OUT OF REACH OF CHILDREN - FOR ORAL USE ONLY"
    },
    {
        "pharmacy": "RIVERBEND HEALTH PHARMACY #204 - (555) 349-8120",
        "pharm_address": "450 BROADWAY, BOSTON, MA 02116",
        "rx_num": "RX # 7812903-4512",
        "date": "11/18/2026",
        "patient": "PATIENT: JAMES SULLIVAN",
        "doctor": "DR: DR. SARAH JENKINS, MD",
        "drug_line": "METFORMIN HCL 500 MG TABLET",
        "directions": "TAKE 1 TABLET BY MOUTH TWICE DAILY WITH MORNING AND EVENING MEALS",
        "warning": "WARNING: TAKE WITH FOOD TO REDUCE STOMACH UPSET",
        "qty_refills": "QTY: 60 TABLETS   REFILLS: 3   EXP: 10/2027",
        "ndc_mfr": "NDC: 65862-009-60   AUROBINDO PHARMA",
        "target_drug_dose": "Metformin 500mg",
        "footer": "KEEP OUT OF REACH OF CHILDREN - FOR ORAL USE ONLY"
    },
    {
        "pharmacy": "OAKVALE COMMUNITY RX #305 - (555) 902-1144",
        "pharm_address": "820 MARKET ST, PHILADELPHIA, PA 19107",
        "rx_num": "RX # 4901283-7721",
        "date": "11/15/2026",
        "patient": "PATIENT: MARCUS VANCE",
        "doctor": "DR: DR. EMILY CHEN, MD",
        "drug_line": "LISINOPRIL 10 MG TABLET",
        "directions": "TAKE 1 TABLET BY MOUTH DAILY IN THE MORNING",
        "warning": "WARNING: DO NOT DISCONTINUE WITHOUT CONSULTING PHYSICIAN",
        "qty_refills": "QTY: 30 TABLETS   REFILLS: 5   EXP: 11/2027",
        "ndc_mfr": "NDC: 68180-514-01   LUPIN PHARMACEUTICALS",
        "target_drug_dose": "Lisinopril 10mg",
        "footer": "KEEP OUT OF REACH OF CHILDREN - FOR ORAL USE ONLY"
    },
    {
        "pharmacy": "SUMMIT CREST PHARMACY #412 - (555) 671-2098",
        "pharm_address": "12 J.N. ROAD, MUMBAI, MH 400001",
        "rx_num": "RX # 9021844-3310",
        "date": "11/19/2026",
        "patient": "PATIENT: ARJUN MEHTA",
        "doctor": "DR: DR. RAJESH SHARMA, MBBS",
        "drug_line": "ATORVASTATIN CALCIUM 20 MG TABLET",
        "directions": "TAKE 1 TABLET BY MOUTH DAILY AT BEDTIME",
        "warning": "WARNING: AVOID GRAPEFRUIT JUICE WHILE TAKING THIS MEDICATION",
        "qty_refills": "QTY: 30 TABLETS   REFILLS: 2   EXP: 09/2027",
        "ndc_mfr": "NDC: 0093-5058-01   TEVA PHARMACEUTICALS",
        "target_drug_dose": "Atorvastatin 20mg",
        "footer": "KEEP OUT OF REACH OF CHILDREN - FOR ORAL USE ONLY"
    },
    {
        "pharmacy": "BEACON HILL MEDICAL RX #519 - (555) 438-9901",
        "pharm_address": "200 COMMERCIAL BLVD, CHICAGO, IL 60611",
        "rx_num": "RX # 3319028-1123",
        "date": "11/14/2026",
        "patient": "PATIENT: CLARA OSWALD",
        "doctor": "DR: DR. DAVID TENNANT, MD",
        "drug_line": "LEVOTHYROXINE SODIUM 50 MCG TABLET",
        "directions": "TAKE 1 TABLET DAILY IN MORNING 30 MINUTES BEFORE BREAKFAST",
        "warning": "WARNING: TAKE ON EMPTY STOMACH WITH FULL GLASS OF WATER",
        "qty_refills": "QTY: 90 TABLETS   REFILLS: 1   EXP: 08/2027",
        "ndc_mfr": "NDC: 0074-6624-11   ABBVIE INC",
        "target_drug_dose": "Levothyroxine 50mcg",
        "footer": "KEEP OUT OF REACH OF CHILDREN - FOR ORAL USE ONLY"
    },
    {
        "pharmacy": "PINE VALLEY PHARMACY #602 - (555) 771-4450",
        "pharm_address": "55 LINK ROAD, BANDRA, MUMBAI 400050",
        "rx_num": "RX # 8820194-5561",
        "date": "11/17/2026",
        "patient": "PATIENT: PRIYA NAIR",
        "doctor": "DR: DR. ANITA DESAI, MD",
        "drug_line": "AMLODIPINE BESYLATE 5 MG TABLET",
        "directions": "TAKE 1 TABLET BY MOUTH ONCE DAILY WITH OR WITHOUT FOOD",
        "warning": "WARNING: MAY CAUSE DIZZINESS WHEN RISING FROM SITTING POSITION",
        "qty_refills": "QTY: 30 TABLETS   REFILLS: 4   EXP: 11/2027",
        "ndc_mfr": "NDC: 55111-180-30   VIATRIS SPECIALTY",
        "target_drug_dose": "Amlodipine 5mg",
        "footer": "KEEP OUT OF REACH OF CHILDREN - FOR ORAL USE ONLY"
    },
    {
        "pharmacy": "CEDAR SPRINGS PHARMACY #718 - (555) 880-3321",
        "pharm_address": "14 OXFORD ST, LONDON, W1D 1BS",
        "rx_num": "RX # 5510294-8872",
        "date": "11/16/2026",
        "patient": "PATIENT: ARTHUR DENT",
        "doctor": "DR: DR. FORD PREFECT, MD",
        "drug_line": "OMEPRAZOLE 20 MG DELAYED RELEASE CAPSULE",
        "directions": "TAKE 1 CAPSULE DAILY IN THE MORNING BEFORE FIRST MEAL",
        "warning": "WARNING: SWALLOW WHOLE DO NOT CRUSH OR CHEW CAPSULE",
        "qty_refills": "QTY: 28 CAPSULES   REFILLS: 0   EXP: 12/2027",
        "ndc_mfr": "NDC: 0781-2234-01   SANDOZ INC",
        "target_drug_dose": "Omeprazole 20mg",
        "footer": "KEEP OUT OF REACH OF CHILDREN - FOR ORAL USE ONLY"
    },
    {
        "pharmacy": "HORIZON APOTHECARY #803 - (555) 662-9018",
        "pharm_address": "700 GATEWAY PARK, SAN FRANCISCO, CA 94103",
        "rx_num": "RX # 6610928-3419",
        "date": "11/19/2026",
        "patient": "PATIENT: NATHAN DRAKE",
        "doctor": "DR: DR. VICTOR SULLIVAN, MD",
        "drug_line": "LOSARTAN POTASSIUM 50 MG TABLET",
        "directions": "TAKE 1 TABLET BY MOUTH DAILY AS DIRECTED FOR BLOOD PRESSURE",
        "warning": "WARNING: DO NOT TAKE IF PREGNANT CONSULT PHYSICIAN",
        "qty_refills": "QTY: 30 TABLETS   REFILLS: 3   EXP: 11/2027",
        "ndc_mfr": "NDC: 31722-701-30   CAMBER PHARMACEUTICALS",
        "target_drug_dose": "Losartan 50mg",
        "footer": "KEEP OUT OF REACH OF CHILDREN - FOR ORAL USE ONLY"
    },
    {
        "pharmacy": "HARBORVIEW CARE PHARMACY #915 - (555) 234-5590",
        "pharm_address": "330 NICOLLET MALL, MINNEAPOLIS, MN 55401",
        "rx_num": "RX # 4409182-1209",
        "date": "11/12/2026",
        "patient": "PATIENT: BRUCE WAYNE",
        "doctor": "DR: DR. LESLIE THOMPKINS, MD",
        "drug_line": "GABAPENTIN 300 MG CAPSULE",
        "directions": "TAKE 1 CAPSULE BY MOUTH THREE TIMES DAILY FOR NERVE PAIN",
        "warning": "WARNING: MAY CAUSE DROWSINESS DO NOT OPERATE MACHINERY",
        "qty_refills": "QTY: 90 CAPSULES   REFILLS: 1   EXP: 10/2027",
        "ndc_mfr": "NDC: 65862-200-90   AUROBINDO PHARMA",
        "target_drug_dose": "Gabapentin 300mg",
        "footer": "KEEP OUT OF REACH OF CHILDREN - FOR ORAL USE ONLY"
    },
    {
        "pharmacy": "HIGHLAND WELLNESS RX #114 - (555) 991-8843",
        "pharm_address": "120 VINE ST, CINCINNATI, OH 45202",
        "rx_num": "RX # 7710293-8841",
        "date": "11/18/2026",
        "patient": "PATIENT: DIANA PRINCE",
        "doctor": "DR: DR. PATRICIA MINERVA, MD",
        "drug_line": "SERTRALINE HCL 50 MG TABLET",
        "directions": "TAKE 1 TABLET BY MOUTH ONCE DAILY IN THE MORNING",
        "warning": "WARNING: DO NOT STOP TAKING WITHOUT TALKING TO DOCTOR",
        "qty_refills": "QTY: 30 TABLETS   REFILLS: 5   EXP: 11/2027",
        "ndc_mfr": "NDC: 69097-834-12   CIPLA USA INC",
        "target_drug_dose": "Sertraline 50mg",
        "footer": "KEEP OUT OF REACH OF CHILDREN - FOR ORAL USE ONLY"
    },
    {
        "pharmacy": "LAKESIDE PHARMACY #228 - (555) 345-6712",
        "pharm_address": "500 QUEEN ANNE AVE, SEATTLE, WA 98109",
        "rx_num": "RX # 5509182-7740",
        "date": "11/17/2026",
        "patient": "PATIENT: BARRY ALLEN",
        "doctor": "DR: DR. CAITLIN SNOW, MD",
        "drug_line": "SIMVASTATIN 20 MG TABLET",
        "directions": "TAKE 1 TABLET BY MOUTH DAILY IN THE EVENING WITH WATER",
        "warning": "WARNING: REPORT ANY UNEXPLAINED MUSCLE PAIN IMMEDIATELY",
        "qty_refills": "QTY: 30 TABLETS   REFILLS: 2   EXP: 10/2027",
        "ndc_mfr": "NDC: 71335-3197-1   BRYANT RANCH PREPACK",
        "target_drug_dose": "Simvastatin 20mg",
        "footer": "KEEP OUT OF REACH OF CHILDREN - FOR ORAL USE ONLY"
    },
    {
        "pharmacy": "SUNSET PLAZA APOTHECARY #339 - (555) 881-2390",
        "pharm_address": "100 BISCAYNE BLVD, MIAMI, FL 33132",
        "rx_num": "RX # 9910284-4412",
        "date": "11/19/2026",
        "patient": "PATIENT: PETER PARKER",
        "doctor": "DR: DR. CURT CONNORS, MD",
        "drug_line": "MONTELUKAST SODIUM 10 MG TABLET",
        "directions": "TAKE 1 TABLET BY MOUTH DAILY IN THE EVENING FOR ASTHMA",
        "warning": "WARNING: TAKE EVERY DAY EVEN WHEN ASTHMA SYMPTOMS IMPROVE",
        "qty_refills": "QTY: 30 TABLETS   REFILLS: 3   EXP: 11/2027",
        "ndc_mfr": "NDC: 43063-762-30   PD-RX PHARMACEUTICALS",
        "target_drug_dose": "Montelukast 10mg",
        "footer": "KEEP OUT OF REACH OF CHILDREN - FOR ORAL USE ONLY"
    },
    {
        "pharmacy": "CRESTVIEW HEALTH RX #442 - (555) 441-9982",
        "pharm_address": "880 WOODWARD AVE, DETROIT, MI 48226",
        "rx_num": "RX # 2210948-5510",
        "date": "11/16/2026",
        "patient": "PATIENT: TONY STARK",
        "doctor": "DR: DR. HELEN CHO, MD",
        "drug_line": "ESCITALOPRAM OXALATE 10 MG TABLET",
        "directions": "TAKE 1 TABLET BY MOUTH DAILY IN MORNING OR EVENING",
        "warning": "WARNING: MAY TAKE 1 TO 4 WEEKS FOR FULL BENEFIT",
        "qty_refills": "QTY: 30 TABLETS   REFILLS: 4   EXP: 09/2027",
        "ndc_mfr": "NDC: 68180-135-01   LUPIN PHARMACEUTICALS",
        "target_drug_dose": "Escitalopram 10mg",
        "footer": "KEEP OUT OF REACH OF CHILDREN - FOR ORAL USE ONLY"
    },
    {
        "pharmacy": "VALLEY GREEN PHARMACY #551 - (555) 772-1092",
        "pharm_address": "300 PENN AVE, PITTSBURGH, PA 15222",
        "rx_num": "RX # 3310984-7711",
        "date": "11/15/2026",
        "patient": "PATIENT: STEVE ROGERS",
        "doctor": "DR: DR. ABRAHAM ERSKINE, MD",
        "drug_line": "ACETAMINOPHEN 500 MG EXTRA STRENGTH TABLET",
        "directions": "TAKE 2 TABLETS EVERY 6 HOURS AS NEEDED FOR PAIN",
        "warning": "WARNING: DO NOT EXCEED 6 TABLETS IN 24 HOURS LIVER WARNING",
        "qty_refills": "QTY: 50 TABLETS   REFILLS: 0   EXP: 12/2027",
        "ndc_mfr": "NDC: 55289-563-30   PD-RX PHARMACEUTICALS",
        "target_drug_dose": "Acetaminophen 500mg",
        "footer": "KEEP OUT OF REACH OF CHILDREN - FOR ORAL USE ONLY"
    },
    {
        "pharmacy": "BLUE RIDGE MEDICAL PHARMACY #663 - (555) 332-9011",
        "pharm_address": "1750 EAST AVE, ROCHESTER, NY 14610",
        "rx_num": "RX # 8810294-3321",
        "date": "11/18/2026",
        "patient": "PATIENT: NATASHA ROMANOFF",
        "doctor": "DR: DR. SAMUEL STERN, MD",
        "drug_line": "IBUPROFEN 200 MG TABLET",
        "directions": "TAKE 1 TABLET BY MOUTH EVERY 4 TO 6 HOURS WITH FOOD FOR PAIN",
        "warning": "WARNING: TAKE WITH FOOD OR MILK TO PREVENT STOMACH UPSET",
        "qty_refills": "QTY: 40 TABLETS   REFILLS: 1   EXP: 11/2027",
        "ndc_mfr": "NDC: 0573-0164-40   PFIZER CONSUMER",
        "target_drug_dose": "Ibuprofen 200mg",
        "footer": "KEEP OUT OF REACH OF CHILDREN - FOR ORAL USE ONLY"
    },
    {
        "pharmacy": "NORTH STAR APOTHECARY #774 - (555) 882-1049",
        "pharm_address": "1000 S CONGRESS AVE, AUSTIN, TX 78704",
        "rx_num": "RX # 4410928-6623",
        "date": "11/14/2026",
        "patient": "PATIENT: WANDA MAXIMOFF",
        "doctor": "DR: DR. STEPHEN STRANGE, MD",
        "drug_line": "ALBUTEROL SULFATE 90 MCG INHALATION AEROSOL",
        "directions": "INHALE 2 PUFFS BY MOUTH EVERY 4 TO 6 HOURS AS NEEDED FOR WHEEZING",
        "warning": "WARNING: SHAKE WELL BEFORE USE RINSE MOUTH AFTER INHALING",
        "qty_refills": "QTY: 1 CANISTER   REFILLS: 2   EXP: 08/2027",
        "ndc_mfr": "NDC: 0487-9501-01   NEPHRON PHARMACEUTICALS",
        "target_drug_dose": "Albuterol 90mcg",
        "footer": "KEEP OUT OF REACH OF CHILDREN - FOR ORAL INHALATION ONLY"
    },
    {
        "pharmacy": "WEST END CARE PHARMACY #885 - (555) 901-2244",
        "pharm_address": "400 S TRYON ST, CHARLOTTE, NC 28285",
        "rx_num": "RX # 6610294-8831",
        "date": "11/16/2026",
        "patient": "PATIENT: SAM WILSON",
        "doctor": "DR: DR. JONATHAN VALE, MD",
        "drug_line": "FLUTICASONE PROPIONATE 50 MCG NASAL SPRAY",
        "directions": "SPRAY 2 SPRAYS IN EACH NOSTRIL ONCE DAILY FOR ALLERGIES",
        "warning": "WARNING: SHAKE GENTLY BEFORE USE FOR INTRANASAL USE ONLY",
        "qty_refills": "QTY: 1 BOTTLE   REFILLS: 3   EXP: 10/2027",
        "ndc_mfr": "NDC: 0054-3270-99   HIKMA PHARMACEUTICALS",
        "target_drug_dose": "Fluticasone 50mcg",
        "footer": "KEEP OUT OF REACH OF CHILDREN - FOR INTRANASAL USE ONLY"
    },
    {
        "pharmacy": "MAPLE GROVE PHARMACY #996 - (555) 229-3381",
        "pharm_address": "410 6TH AVE, DES MOINES, IA 50309",
        "rx_num": "RX # 7710294-9912",
        "date": "11/17/2026",
        "patient": "PATIENT: SCOTT LANG",
        "doctor": "DR: DR. HANK PYM, MD",
        "drug_line": "PANTOPRAZOLE SODIUM 40 MG DELAYED RELEASE TABLET",
        "directions": "TAKE 1 TABLET BY MOUTH DAILY 30 MINUTES BEFORE BREAKFAST",
        "warning": "WARNING: SWALLOW WHOLE DO NOT SPLIT CRUSH OR CHEW",
        "qty_refills": "QTY: 30 TABLETS   REFILLS: 2   EXP: 11/2027",
        "ndc_mfr": "NDC: 55154-4225-5   CARDINAL HEALTH",
        "target_drug_dose": "Pantoprazole 40mg",
        "footer": "KEEP OUT OF REACH OF CHILDREN - FOR ORAL USE ONLY"
    },
    {
        "pharmacy": "CENTRAL VALLEY RX #107 - (555) 883-4410",
        "pharm_address": "100 BURNSIDE ST, PORTLAND, OR 97209",
        "rx_num": "RX # 3310294-5519",
        "date": "11/19/2026",
        "patient": "PATIENT: MATT MURDOCK",
        "doctor": "DR: DR. CLAIRE TEMPLE, MD",
        "drug_line": "FUROSEMIDE 20 MG TABLET",
        "directions": "TAKE 1 TABLET BY MOUTH DAILY IN THE MORNING WITH WATER",
        "warning": "WARNING: TAKE IN MORNING TO AVOID SLEEP INTERRUPTION",
        "qty_refills": "QTY: 30 TABLETS   REFILLS: 1   EXP: 09/2027",
        "ndc_mfr": "NDC: 0054-4297-25   HIKMA PHARMACEUTICALS",
        "target_drug_dose": "Furosemide 20mg",
        "footer": "KEEP OUT OF REACH OF CHILDREN - FOR ORAL USE ONLY"
    },
    {
        "pharmacy": "SILVER LAKE APOTHECARY #218 - (555) 661-8822",
        "pharm_address": "100 WALL ST, NEW YORK, NY 10005",
        "rx_num": "RX # 5510293-4401",
        "date": "11/20/2026",
        "patient": "PATIENT: JESSICA JONES",
        "doctor": "DR: DR. TRISH WALKER, MD",
        "drug_line": "PREDNISONE 10 MG TABLET",
        "directions": "TAKE 2 TABLETS BY MOUTH DAILY IN MORNING WITH FOOD FOR 5 DAYS",
        "warning": "WARNING: TAKE WITH FOOD TO PREVENT STOMACH IRRITATION",
        "qty_refills": "QTY: 10 TABLETS   REFILLS: 0   EXP: 08/2027",
        "ndc_mfr": "NDC: 0054-0017-25   HIKMA PHARMACEUTICALS",
        "target_drug_dose": "Prednisone 10mg",
        "footer": "KEEP OUT OF REACH OF CHILDREN - FOR ORAL USE ONLY"
    }
]

def render_prescription_label(spec, output_path):
    img = Image.new('RGB', (750, 480), color=(253, 253, 251))
    draw = ImageDraw.Draw(img)

    # Frame border
    draw.rectangle([8, 8, 742, 472], outline=(160, 160, 160), width=2)
    # Header bar
    draw.rectangle([8, 8, 742, 65], fill=(210, 35, 45))
    draw.text((25, 18), spec["pharmacy"], fill=(255, 255, 255))
    draw.text((25, 38), spec["pharm_address"], fill=(255, 255, 255))

    # Rx & Patient block
    draw.text((25, 85), f"{spec['rx_num']}   DATE: {spec['date']}", fill=(20, 20, 20))
    draw.text((25, 112), spec["patient"], fill=(20, 20, 20))
    draw.text((25, 138), spec["doctor"], fill=(20, 20, 20))

    # Prominent medication line
    draw.line([20, 170, 730, 170], fill=(200, 200, 200), width=1)
    draw.text((25, 185), spec["drug_line"], fill=(0, 0, 0))
    draw.line([20, 220, 730, 220], fill=(200, 200, 200), width=1)

    # Directions
    draw.text((25, 235), spec["directions"], fill=(10, 10, 10))
    draw.text((25, 275), spec["warning"], fill=(90, 90, 90))

    # Qty, refills, NDC
    draw.text((25, 325), spec["qty_refills"], fill=(20, 20, 20))
    draw.text((25, 360), spec["ndc_mfr"], fill=(40, 40, 40))
    
    # Specific route footer (inhaler vs nasal spray vs oral)
    footer_text = spec.get("footer", "KEEP OUT OF REACH OF CHILDREN - FOR ORAL USE ONLY")
    draw.text((25, 410), footer_text, fill=(140, 20, 20))

    img.save(output_path, quality=95)
    return output_path

def build_dataset(output_dir="assets/prescription_labels"):
    os.makedirs(output_dir, exist_ok=True)
    manifest = []
    
    for idx, spec in enumerate(PRESCRIPTION_SPECS):
        img_name = f"prescription_{idx+1:02d}_{spec['target_drug_dose'].replace(' ', '_').lower()}.jpg"
        img_path = os.path.join(output_dir, img_name)
        render_prescription_label(spec, img_path)
        
        footer_text = spec.get("footer", "KEEP OUT OF REACH OF CHILDREN - FOR ORAL USE ONLY")
        ground_truth_text = (
            f"{spec['pharmacy']} {spec['pharm_address']} "
            f"{spec['rx_num']} DATE: {spec['date']} "
            f"{spec['patient']} {spec['doctor']} "
            f"{spec['drug_line']} {spec['directions']} {spec['warning']} "
            f"{spec['qty_refills']} {spec['ndc_mfr']} "
            f"{footer_text}"
        )
        
        manifest.append({
            "id": idx + 1,
            "image_path": img_path,
            "drug_line": spec["drug_line"],
            "target_extraction": spec["target_drug_dose"],
            "ground_truth_ocr": ground_truth_text,
            "footer": footer_text
        })
        print(f"Generated Label #{idx+1:02d}: {spec['target_drug_dose']:22s} -> {img_path}")
        
    manifest_path = os.path.join(output_dir, "prescription_manifest.json")
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"\n[✓] Successfully compiled 20 Realistic Prescription Labels with Ground Truth: {manifest_path}")
    return manifest

if __name__ == "__main__":
    build_dataset()
