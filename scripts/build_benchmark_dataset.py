"""
PROJECT FRIDAY: STANDARDIZED 40-SAMPLE MULTIMODAL BENCHMARK DATASET BUILDER
Generates 40 distinct photographic benchmark samples across 4 categories:
1. Medicine / Product labels (10 samples)
2. Signage / Menu boards (10 samples)
3. Documents / Invoices / Textbook pages (10 samples)
4. Real-world scenes with environmental text (10 samples)

Preserves exact punctuation, case, numbers, and key clinical/navigational entities.
"""

import os
import json
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BENCHMARK_SPECS = [
    # -------------------------------------------------------------
    # 1. MEDICINE (10 Samples)
    # -------------------------------------------------------------
    {
        "id": "med_01",
        "category": "medicine",
        "title": "Amoxicillin 500mg Capsule Bottle",
        "distance_cm": 35,
        "focus_quality": "in_focus",
        "lines": [
            "METROPOLIS RX #101 - (555) 019-2834",
            "RX # 6543210-0987   DATE: 11/20/2026",
            "PATIENT: ELEANOR RIGBY",
            "AMOXICILLIN 500 MG CAPSULE",
            "TAKE 1 CAPSULE BY MOUTH TWICE DAILY FOR 10 DAYS",
            "QTY: 20 CAPSULES   EXP: 11/2027",
            "KEEP OUT OF REACH OF CHILDREN - FOR ORAL USE ONLY"
        ],
        "key_field_type": "drug_and_dose",
        "key_field_value": "Amoxicillin 500mg",
        "prompt": "What medication is this and what is the prescribed dose?",
        "expected_safety_entity": "500mg",
        "bg_color": (245, 244, 240)
    },
    {
        "id": "med_02",
        "category": "medicine",
        "title": "Metformin 500mg Extended Release",
        "distance_cm": 35,
        "lines": [
            "RIVERBEND HEALTH PHARMACY #204",
            "RX # 7812903-4512   DATE: 11/18/2026",
            "PATIENT: JAMES SULLIVAN",
            "METFORMIN HCL 500 MG TABLET",
            "TAKE 1 TABLET TWICE DAILY WITH MEALS",
            "QTY: 60 TABLETS   EXP: 10/2027",
            "KEEP OUT OF REACH OF CHILDREN - FOR ORAL USE ONLY"
        ],
        "key_field_type": "drug_and_dose",
        "key_field_value": "Metformin 500mg",
        "prompt": "What medication is this and what is the prescribed dose?",
        "expected_safety_entity": "500mg",
        "bg_color": (248, 247, 242)
    },
    {
        "id": "med_03",
        "category": "medicine",
        "title": "Lisinopril 10mg Blood Pressure Tablet",
        "distance_cm": 35,
        "lines": [
            "OAKVALE COMMUNITY RX #305",
            "RX # 4901283-7721   DATE: 11/15/2026",
            "PATIENT: MARCUS VANCE",
            "LISINOPRIL 10 MG TABLET",
            "TAKE 1 TABLET DAILY IN THE MORNING",
            "QTY: 30 TABLETS   EXP: 11/2027",
            "KEEP OUT OF REACH OF CHILDREN - FOR ORAL USE ONLY"
        ],
        "key_field_type": "drug_and_dose",
        "key_field_value": "Lisinopril 10mg",
        "prompt": "What medication is this and what is the prescribed dose?",
        "expected_safety_entity": "10mg",
        "bg_color": (244, 245, 242)
    },
    {
        "id": "med_04",
        "category": "medicine",
        "title": "Atorvastatin 20mg Cholesterol Tablet",
        "distance_cm": 35,
        "lines": [
            "SUMMIT CREST PHARMACY #412",
            "RX # 9021844-3310   DATE: 11/19/2026",
            "PATIENT: ARJUN MEHTA",
            "ATORVASTATIN CALCIUM 20 MG TABLET",
            "TAKE 1 TABLET DAILY AT BEDTIME",
            "QTY: 30 TABLETS   EXP: 09/2027",
            "KEEP OUT OF REACH OF CHILDREN - FOR ORAL USE ONLY"
        ],
        "key_field_type": "drug_and_dose",
        "key_field_value": "Atorvastatin 20mg",
        "prompt": "What medication is this and what is the prescribed dose?",
        "expected_safety_entity": "20mg",
        "bg_color": (246, 244, 240)
    },
    {
        "id": "med_05",
        "category": "medicine",
        "title": "Levothyroxine 50mcg Thyroid Hormone",
        "distance_cm": 35,
        "lines": [
            "BEACON HILL MEDICAL RX #519",
            "RX # 3319028-1123   DATE: 11/14/2026",
            "PATIENT: CLARA OSWALD",
            "LEVOTHYROXINE SODIUM 50 MCG TABLET",
            "TAKE 1 TABLET DAILY 30 MINUTES BEFORE BREAKFAST",
            "QTY: 90 TABLETS   EXP: 08/2027",
            "KEEP OUT OF REACH OF CHILDREN - FOR ORAL USE ONLY"
        ],
        "key_field_type": "drug_and_dose",
        "key_field_value": "Levothyroxine 50mcg",
        "prompt": "What medication is this and what is the prescribed dose?",
        "expected_safety_entity": "50mcg",
        "bg_color": (247, 246, 241)
    },
    {
        "id": "med_06",
        "category": "medicine",
        "title": "Amlodipine 5mg Calcium Channel Blocker",
        "distance_cm": 35,
        "lines": [
            "PINE VALLEY PHARMACY #602",
            "RX # 8820194-5561   DATE: 11/17/2026",
            "PATIENT: PRIYA NAIR",
            "AMLODIPINE BESYLATE 5 MG TABLET",
            "TAKE 1 TABLET ONCE DAILY WITH WATER",
            "QTY: 30 TABLETS   EXP: 11/2027",
            "KEEP OUT OF REACH OF CHILDREN - FOR ORAL USE ONLY"
        ],
        "key_field_type": "drug_and_dose",
        "key_field_value": "Amlodipine 5mg",
        "prompt": "What medication is this and what is the prescribed dose?",
        "expected_safety_entity": "5mg",
        "bg_color": (245, 243, 239)
    },
    {
        "id": "med_07",
        "category": "medicine",
        "title": "Omeprazole 20mg Delayed Release",
        "distance_cm": 35,
        "lines": [
            "CEDAR SPRINGS PHARMACY #718",
            "RX # 5510294-8872   DATE: 11/16/2026",
            "PATIENT: ARTHUR DENT",
            "OMEPRAZOLE 20 MG DELAYED RELEASE CAPSULE",
            "TAKE 1 CAPSULE DAILY BEFORE BREAKFAST",
            "QTY: 28 CAPSULES   EXP: 12/2027",
            "KEEP OUT OF REACH OF CHILDREN - FOR ORAL USE ONLY"
        ],
        "key_field_type": "drug_and_dose",
        "key_field_value": "Omeprazole 20mg",
        "prompt": "What medication is this and what is the prescribed dose?",
        "expected_safety_entity": "20mg",
        "bg_color": (248, 245, 242)
    },
    {
        "id": "med_08",
        "category": "medicine",
        "title": "Gabapentin 300mg Nerve Pain Capsule",
        "distance_cm": 35,
        "lines": [
            "HARBORVIEW CARE PHARMACY #915",
            "RX # 4409182-1209   DATE: 11/12/2026",
            "PATIENT: BRUCE WAYNE",
            "GABAPENTIN 300 MG CAPSULE",
            "TAKE 1 CAPSULE THREE TIMES DAILY FOR NERVE PAIN",
            "QTY: 90 CAPSULES   EXP: 10/2027",
            "KEEP OUT OF REACH OF CHILDREN - FOR ORAL USE ONLY"
        ],
        "key_field_type": "drug_and_dose",
        "key_field_value": "Gabapentin 300mg",
        "prompt": "What medication is this and what is the prescribed dose?",
        "expected_safety_entity": "300mg",
        "bg_color": (244, 246, 243)
    },
    {
        "id": "med_09",
        "category": "medicine",
        "title": "Albuterol 90mcg Inhalation Aerosol",
        "distance_cm": 35,
        "lines": [
            "NORTH STAR APOTHECARY #774",
            "RX # 4410928-6623   DATE: 11/14/2026",
            "PATIENT: WANDA MAXIMOFF",
            "ALBUTEROL SULFATE 90 MCG INHALATION AEROSOL",
            "INHALE 2 PUFFS EVERY 4 TO 6 HOURS AS NEEDED",
            "QTY: 1 CANISTER   EXP: 08/2027",
            "KEEP OUT OF REACH OF CHILDREN - FOR ORAL INHALATION ONLY"
        ],
        "key_field_type": "drug_and_dose",
        "key_field_value": "Albuterol 90mcg",
        "prompt": "What medication is this and what is the prescribed dose?",
        "expected_safety_entity": "90mcg",
        "bg_color": (243, 245, 247)
    },
    {
        "id": "med_10",
        "category": "medicine",
        "title": "Fluticasone 50mcg Nasal Spray",
        "distance_cm": 35,
        "lines": [
            "WEST END CARE PHARMACY #885",
            "RX # 6610294-8831   DATE: 11/16/2026",
            "PATIENT: SAM WILSON",
            "FLUTICASONE PROPIONATE 50 MCG NASAL SPRAY",
            "SPRAY 2 SPRAYS IN EACH NOSTRIL ONCE DAILY",
            "QTY: 1 BOTTLE   EXP: 10/2027",
            "KEEP OUT OF REACH OF CHILDREN - FOR INTRANASAL USE ONLY"
        ],
        "key_field_type": "drug_and_dose",
        "key_field_value": "Fluticasone 50mcg",
        "prompt": "What medication is this and what is the prescribed dose?",
        "expected_safety_entity": "50mcg",
        "bg_color": (245, 247, 244)
    },

    # -------------------------------------------------------------
    # 2. SIGNAGE & MENUS (10 Samples)
    # -------------------------------------------------------------
    {
        "id": "sign_01",
        "category": "signage_menu",
        "title": "Artisan Coffee House Menu Board",
        "distance_cm": 38,
        "lines": [
            "ARTISAN COFFEE ROASTERS",
            "ESPRESSO ................. $3.50",
            "AMERICANO ................ $4.00",
            "COLD BREW ................ $4.75",
            "OAT MILK LATTE ........... $5.50",
            "ALL PRICES INCLUDE TAX"
        ],
        "key_field_type": "menu_price",
        "key_field_value": "Cold Brew $4.75",
        "prompt": "What is the price of Cold Brew on this menu?",
        "expected_safety_entity": "$4.75",
        "bg_color": (35, 38, 42),
        "text_color": (245, 240, 230)
    },
    {
        "id": "sign_02",
        "category": "signage_menu",
        "title": "Subway Station Directional Sign",
        "distance_cm": 40,
        "lines": [
            "METROPOLITAN TRANSIT AUTHORITY",
            "DOWNTOWN & BROOKLYN EXPRESS",
            "TRAINS A, C, E -> TRACK 2",
            "UPTOWN & BRONX -> TRACK 1",
            "ACCESSIBLE ELEVATOR AT CONCOURSE LEVEL"
        ],
        "key_field_type": "transit_direction",
        "key_field_value": "Trains A, C, E -> Track 2",
        "prompt": "Which track do the downtown express trains arrive on?",
        "expected_safety_entity": "Track 2",
        "bg_color": (25, 45, 80),
        "text_color": (255, 255, 255)
    },
    {
        "id": "sign_03",
        "category": "signage_menu",
        "title": "Bakery Pastry Pricing Board",
        "distance_cm": 35,
        "lines": [
            "LE PETIT PAIN ARTISAN BAKERY",
            "BUTTER CROISSANT ......... $3.25",
            "PAIN AU CHOCOLAT ......... $3.85",
            "ALMOND CROISSANT ......... $4.50",
            "CINNAMON ROLL ............ $4.00"
        ],
        "key_field_type": "menu_price",
        "key_field_value": "Almond Croissant $4.50",
        "prompt": "How much does the almond croissant cost?",
        "expected_safety_entity": "$4.50",
        "bg_color": (248, 244, 235),
        "text_color": (40, 30, 20)
    },
    {
        "id": "sign_04",
        "category": "signage_menu",
        "title": "Hospital Department Directory Sign",
        "distance_cm": 38,
        "lines": [
            "ST. JUDE MEDICAL CENTER - 3RD FLOOR",
            "CARDIOLOGY CLINIC ......... ROOM 301",
            "NEUROLOGY SUITE ........... ROOM 308",
            "DIAGNOSTIC IMAGING ........ ROOM 315",
            "PHARMACY DISPENSARY ....... ROOM 320"
        ],
        "key_field_type": "directory_room",
        "key_field_value": "Cardiology Clinic Room 301",
        "prompt": "Which room number is the Cardiology Clinic?",
        "expected_safety_entity": "Room 301",
        "bg_color": (240, 245, 248),
        "text_color": (15, 35, 60)
    },
    {
        "id": "sign_05",
        "category": "signage_menu",
        "title": "Airport Departure Gate Sign",
        "distance_cm": 40,
        "lines": [
            "INTERNATIONAL TERMINAL B",
            "GATE B24 - ON TIME",
            "FLIGHT AI 102 -> LONDON HEATHROW",
            "BOARDING ZONE 1 AT 14:15",
            "FINAL CALL AT 14:40"
        ],
        "key_field_type": "flight_gate",
        "key_field_value": "Gate B24 - Flight AI 102",
        "prompt": "What is the departure gate and flight number?",
        "expected_safety_entity": "Gate B24",
        "bg_color": (20, 25, 35),
        "text_color": (255, 220, 50)
    },
    {
        "id": "sign_06",
        "category": "signage_menu",
        "title": "Emergency Exit Caution Notice",
        "distance_cm": 35,
        "lines": [
            "EMERGENCY EXIT ONLY",
            "ALARM WILL SOUND IF DOOR IS OPENED",
            "PUSH TO OPEN - BARRIER FREE",
            "REMAIN CALM AND PROCEED TO STAIRWELL D"
        ],
        "key_field_type": "safety_notice",
        "key_field_value": "Emergency Exit Only",
        "prompt": "What does this door warning notice state?",
        "expected_safety_entity": "Emergency Exit Only",
        "bg_color": (195, 30, 30),
        "text_color": (255, 255, 255)
    },
    {
        "id": "sign_07",
        "category": "signage_menu",
        "title": "Pizzeria Daily Specials Chalkboard",
        "distance_cm": 38,
        "lines": [
            "BELLA NAPOLI PIZZERIA SPECIALS",
            "MARGHERITA PIZZA 12-INCH .... $14.50",
            "PEPPERONI SUPREME 12-INCH .. $16.75",
            "TRUFFLE MUSHROOM 12-INCH ... $18.50",
            "TIRAMISU DESSERT ........... $6.00"
        ],
        "key_field_type": "menu_price",
        "key_field_value": "Margherita Pizza $14.50",
        "prompt": "What is the price of the 12-inch Margherita pizza?",
        "expected_safety_entity": "$14.50",
        "bg_color": (30, 30, 30),
        "text_color": (240, 240, 235)
    },
    {
        "id": "sign_08",
        "category": "signage_menu",
        "title": "Parking Garage Rate Board",
        "distance_cm": 40,
        "lines": [
            "DOWNTOWN CENTRAL PARKING",
            "FIRST 1 HOUR ............... $5.00",
            "UP TO 3 HOURS .............. $12.00",
            "ALL DAY MAXIMUM ............ $25.00",
            "LOST TICKET PAYS ........... $35.00"
        ],
        "key_field_type": "parking_rate",
        "key_field_value": "All Day Maximum $25.00",
        "prompt": "What is the maximum all day parking rate?",
        "expected_safety_entity": "$25.00",
        "bg_color": (235, 240, 245),
        "text_color": (20, 30, 40)
    },
    {
        "id": "sign_09",
        "category": "signage_menu",
        "title": "University Lecture Hall Door Plaque",
        "distance_cm": 35,
        "lines": [
            "DEPARTMENT OF COMPUTER SCIENCE",
            "LECTURE THEATRE CS-104",
            "CAPACITY: 120 SEATS",
            "FACULTY OFFICE HOURS: 14:00 - 16:00 TUE/THU",
            "QUIET STUDY AREA IN CORRIDOR"
        ],
        "key_field_type": "room_number",
        "key_field_value": "Lecture Theatre CS-104",
        "prompt": "Which lecture hall is marked on this plaque?",
        "expected_safety_entity": "CS-104",
        "bg_color": (245, 242, 235),
        "text_color": (35, 30, 25)
    },
    {
        "id": "sign_10",
        "category": "signage_menu",
        "title": "Electric Vehicle Charging Station Sign",
        "distance_cm": 38,
        "lines": [
            "VOLTFAST CHARGING HUB - STALL #04",
            "MAX POWER: 150 KW CCS DC FAST CHARGE",
            "RATE: $0.38 PER KWH + $1.00 SESSION FEE",
            "IDLE FEE AFTER 10 MINS: $0.50/MIN",
            "SUPPORT: 1-800-555-VOLT"
        ],
        "key_field_type": "charging_rate",
        "key_field_value": "Rate: $0.38 per kWh",
        "prompt": "What is the charging rate per kilowatt-hour?",
        "expected_safety_entity": "$0.38",
        "bg_color": (15, 45, 35),
        "text_color": (220, 255, 230)
    },

    # -------------------------------------------------------------
    # 3. DOCUMENTS & INVOICES (10 Samples)
    # -------------------------------------------------------------
    {
        "id": "doc_01",
        "category": "document",
        "title": "Supermarket Grocery Receipt",
        "distance_cm": 35,
        "lines": [
            "METRO MARKET GROCERY - STORE #410",
            "ORGANIC WHOLE MILK 1 GAL ..... $4.29",
            "SOURDOUGH BREAD .............. $3.99",
            "HONEYCRISP APPLES 2.4 LB ..... $5.98",
            "SUBTOTAL: $14.26   TAX: $1.14",
            "TOTAL AMOUNT DUE: $15.40",
            "THANK YOU FOR SHOPPING LOCAL!"
        ],
        "key_field_type": "receipt_total",
        "key_field_value": "Total Amount Due: $15.40",
        "prompt": "What is the final total amount due on this grocery receipt?",
        "expected_safety_entity": "$15.40",
        "bg_color": (250, 250, 248),
        "text_color": (20, 20, 20)
    },
    {
        "id": "doc_02",
        "category": "document",
        "title": "Utility Electric Bill Summary",
        "distance_cm": 36,
        "lines": [
            "PACIFIC POWER & ELECTRIC COMPANY",
            "ACCOUNT #: 9812-4410-02   BILLING PERIOD: OCT 2026",
            "TOTAL CONSUMPTION: 420 KWH @ $0.18/KWH",
            "TRANSMISSION SURCHARGE: $8.40",
            "TOTAL CURRENT CHARGES: $84.00",
            "DUE DATE: 11/30/2026"
        ],
        "key_field_type": "bill_total",
        "key_field_value": "Total Current Charges: $84.00",
        "prompt": "What is the total current charge and due date on this electric bill?",
        "expected_safety_entity": "$84.00",
        "bg_color": (248, 248, 245),
        "text_color": (15, 25, 40)
    },
    {
        "id": "doc_03",
        "category": "document",
        "title": "Technical Textbook Abstract",
        "distance_cm": 35,
        "lines": [
            "DEEP LEARNING ON EMBEDDED EDGE ACCELERATORS",
            "SECTION 4.2: TENSOR MEMORY HIERARCHY",
            "TENSOR CORES STREAM DATA VIA LPDDR5 AT 22.0 GB/S.",
            "WEIGHT QUANTIZATION TO INT4 REDUCES TRAFFIC BY 75%.",
            "TOTAL BANDWIDTH MUST NOT EXCEED 14.0 GB/S CEILING."
        ],
        "key_field_type": "textbook_fact",
        "key_field_value": "Bandwidth must not exceed 14.0 GB/s",
        "prompt": "According to this text, what is the maximum bandwidth ceiling?",
        "expected_safety_entity": "14.0 GB/s",
        "bg_color": (252, 250, 245),
        "text_color": (25, 25, 25)
    },
    {
        "id": "doc_04",
        "category": "document",
        "title": "Hardware Purchase Invoice",
        "distance_cm": 35,
        "lines": [
            "TECHTRONICS HARDWARE SUPPLIES - INVOICE #8812",
            "ITEM 1: ROCKCHIP RK3576 SOM 4GB .... QTY: 1 .. $65.00",
            "ITEM 2: SONY IMX415 4K CAMERA ..... QTY: 1 .. $17.50",
            "ITEM 3: LIPO BATTERY 300MAH ....... QTY: 2 .. $4.50",
            "SHIPPING & HANDLING: $5.00",
            "INVOICE TOTAL: $92.00"
        ],
        "key_field_type": "invoice_total",
        "key_field_value": "Invoice Total: $92.00",
        "prompt": "What is the final invoice total amount?",
        "expected_safety_entity": "$92.00",
        "bg_color": (246, 246, 244),
        "text_color": (20, 20, 20)
    },
    {
        "id": "doc_05",
        "category": "document",
        "title": "Laboratory Blood Test Report",
        "distance_cm": 35,
        "lines": [
            "DIAGNOSTIC PATHOLOGY LAB - PATIENT REF #4419",
            "FASTING BLOOD GLUCOSE: 94 MG/DL (NORMAL: 70 - 99)",
            "HEMOGLOBIN A1C: 5.4% (NORMAL: < 5.7%)",
            "TOTAL CHOLESTEROL: 182 MG/DL (DESIRABLE: < 200)",
            "STATUS: ALL BIOMARKERS WITHIN NORMAL LIMITS"
        ],
        "key_field_type": "lab_value",
        "key_field_value": "Fasting Blood Glucose: 94 mg/dL",
        "prompt": "What is the fasting blood glucose value reported?",
        "expected_safety_entity": "94 mg/dL",
        "bg_color": (250, 252, 250),
        "text_color": (20, 35, 25)
    },
    {
        "id": "doc_06",
        "category": "document",
        "title": "Car Rental Agreement Receipt",
        "distance_cm": 35,
        "lines": [
            "AVALON CAR RENTALS - CONTRACT #5512",
            "VEHICLE: 2026 HYBRID SEDAN - REG # 7XYZ89",
            "DAILY RATE: $45.00 X 3 DAYS = $135.00",
            "COLLISION DAMAGE WAIVER: $30.00",
            "NET TOTAL CHARGED TO CARD: $165.00",
            "RETURN LOCATION: AIRPORT TERMINAL 2"
        ],
        "key_field_type": "receipt_total",
        "key_field_value": "Net Total Charged: $165.00",
        "prompt": "What was the net total amount charged for the car rental?",
        "expected_safety_entity": "$165.00",
        "bg_color": (248, 248, 245),
        "text_color": (20, 20, 20)
    },
    {
        "id": "doc_07",
        "category": "document",
        "title": "Restaurant Dinner Check",
        "distance_cm": 35,
        "lines": [
            "THE OLIVE BISTRO - TABLE 14",
            "1X WILD SALMON FILLET ......... $28.00",
            "1X ROASTED VEGETABLE RISOTTO .. $22.00",
            "2X SPARKLING WATER ............ $8.00",
            "SUBTOTAL: $58.00   TAX: $4.64",
            "TOTAL CHECK: $62.64"
        ],
        "key_field_type": "receipt_total",
        "key_field_value": "Total Check: $62.64",
        "prompt": "What is the total check amount for table 14?",
        "expected_safety_entity": "$62.64",
        "bg_color": (252, 250, 246),
        "text_color": (30, 20, 20)
    },
    {
        "id": "doc_08",
        "category": "document",
        "title": "Academic Research Paper Excerpt",
        "distance_cm": 35,
        "lines": [
            "IEEE TRANSACTIONS ON WEARABLE COMPUTING",
            "EXPERIMENT 3: KNOWLEDGE DISTILLATION CONVERGENCE",
            "STUDENT 415M ACHIEVES 95.2% ACCURACY ON PRESCRIPTIONS.",
            "BOUNDED FORWARD KL LOSS DECREASES FROM 0.134 TO 0.042.",
            "ZERO GRADIENT INSTABILITY OBSERVED OVER 300 STEPS."
        ],
        "key_field_type": "research_finding",
        "key_field_value": "Student 415M achieves 95.2% accuracy",
        "prompt": "What accuracy does the 415M student model achieve in the experiment?",
        "expected_safety_entity": "95.2%",
        "bg_color": (250, 250, 250),
        "text_color": (10, 10, 10)
    },
    {
        "id": "doc_09",
        "category": "document",
        "title": "Pharmaceutical Package Insert Dosage Section",
        "distance_cm": 35,
        "lines": [
            "PRODUCT PRESCRIBING INFORMATION",
            "MAXIMUM ADULT DAILY DOSAGE: 4000 MG PER 24 HOURS.",
            "DO NOT TAKE WITH OTHER ACETAMINOPHEN PRODUCTS.",
            "OVERDOSE WARNING: LIVER DAMAGE RISK IF EXCEEDED.",
            "STORE AT CONTROLLED ROOM TEMPERATURE 20C TO 25C."
        ],
        "key_field_type": "clinical_limit",
        "key_field_value": "Maximum Daily Dosage: 4000 mg",
        "prompt": "What is the maximum allowed daily adult dosage stated in this insert?",
        "expected_safety_entity": "4000 mg",
        "bg_color": (245, 245, 242),
        "text_color": (15, 15, 15)
    },
    {
        "id": "doc_10",
        "category": "document",
        "title": "Bank Wire Transfer Confirmation",
        "distance_cm": 35,
        "lines": [
            "GLOBAL TRUST BANK - DOMESTIC WIRE ADVICE",
            "TRANSFER REF #: TRF-2026-990142",
            "BENEFICIARY: ACME ROBOTICS RESEARCH LTD",
            "WIRE TRANSFER AMOUNT: $2,450.00 USD",
            "PROCESSING FEE: $15.00",
            "STATUS: COMPLETED AND CREDITED"
        ],
        "key_field_type": "transfer_amount",
        "key_field_value": "Wire Amount: $2,450.00 USD",
        "prompt": "What is the transfer reference number and wire amount?",
        "expected_safety_entity": "$2,450.00",
        "bg_color": (248, 250, 252),
        "text_color": (10, 30, 50)
    },

    # -------------------------------------------------------------
    # 4. SCENES WITH ENVIRONMENTAL TEXT (10 Samples)
    # -------------------------------------------------------------
    {
        "id": "scene_01",
        "category": "scene_text",
        "title": "Coffee Shop Counter Front View",
        "distance_cm": 40,
        "lines": [
            "THE DAILY GRIND ROASTERY",
            "ORDER HERE -> PICK UP AT END OF COUNTER",
            "FREE WI-FI NETWORK: DailyGrind_Guest",
            "PASSWORD: FreshCoffee2026"
        ],
        "key_field_type": "wifi_password",
        "key_field_value": "Password: FreshCoffee2026",
        "prompt": "What is the guest Wi-Fi password shown on the counter sign?",
        "expected_safety_entity": "FreshCoffee2026",
        "bg_color": (210, 195, 180),
        "text_color": (30, 20, 10)
    },
    {
        "id": "scene_02",
        "category": "scene_text",
        "title": "Electronics Lab Workstation Test Rig",
        "distance_cm": 38,
        "lines": [
            "RIGID-FLEX TEST BENCH #03",
            "POWER SUPPLY OUTPUT: 5.00V / 2.50A",
            "OSCILLOSCOPE CH1: I2S_BCLK 3.072 MHZ",
            "CH2: I2S_LRCK 48.0 KHZ",
            "WARNING: ESD SENSITIVE WORK AREA"
        ],
        "key_field_type": "bench_voltage",
        "key_field_value": "Output: 5.00V / 2.50A",
        "prompt": "What is the power supply output setting on this test bench?",
        "expected_safety_entity": "5.00V / 2.50A",
        "bg_color": (45, 55, 65),
        "text_color": (120, 255, 150)
    },
    {
        "id": "scene_03",
        "category": "scene_text",
        "title": "Storefront Boutique Signboard",
        "distance_cm": 40,
        "lines": [
            "LUMINA DESIGN STUDIO & GALLERY",
            "OPEN HOURS: 10:00 AM - 7:00 PM MON-SAT",
            "CURATED TIMEPIECES & SMART EYEWEAR",
            "ENTRY THROUGH MAIN GLASS FOYER"
        ],
        "key_field_type": "store_hours",
        "key_field_value": "Hours: 10:00 AM - 7:00 PM",
        "prompt": "What are the open hours for the Lumina Design Studio?",
        "expected_safety_entity": "10:00 AM - 7:00 PM",
        "bg_color": (230, 225, 220),
        "text_color": (25, 25, 30)
    },
    {
        "id": "scene_04",
        "category": "scene_text",
        "title": "Conference Room Glass Door Display",
        "distance_cm": 35,
        "lines": [
            "INNOVATION LAB - MEETING ROOM B",
            "CURRENT RESERVATION: 15:00 - 16:30",
            "TOPIC: PROJECT FRIDAY CAPSTONE DEFENSE",
            "HOST: KRISHNA JAGAT SOLANKI"
        ],
        "key_field_type": "meeting_topic",
        "key_field_value": "Project Friday Capstone Defense",
        "prompt": "What meeting topic is scheduled on this conference room display?",
        "expected_safety_entity": "Project Friday Capstone Defense",
        "bg_color": (30, 35, 45),
        "text_color": (230, 240, 255)
    },
    {
        "id": "scene_05",
        "category": "scene_text",
        "title": "Pharmacy Prescription Drop-Off Window",
        "distance_cm": 38,
        "lines": [
            "PRESCRIPTION DROP-OFF & CONSULTATION",
            "AVERAGE DISPENSING WAIT TIME: 15 MINS",
            "HAVE PHOTO ID AND INSURANCE READY",
            "PHARMACIST ON DUTY: DR. HENDERSON"
        ],
        "key_field_type": "wait_time",
        "key_field_value": "Average Wait Time: 15 Mins",
        "prompt": "What is the average dispensing wait time indicated at the window?",
        "expected_safety_entity": "15 Mins",
        "bg_color": (235, 245, 240),
        "text_color": (20, 50, 40)
    },
    {
        "id": "scene_06",
        "category": "scene_text",
        "title": "Subway Platform Arrival Pillar",
        "distance_cm": 40,
        "lines": [
            "PLATFORM 3 SOUTHBOUND",
            "NEXT TRAIN: TIMES SQUARE 42ND ST",
            "ARRIVING IN: 3 MINUTES",
            "STAND BEHIND YELLOW SAFETY LINE"
        ],
        "key_field_type": "train_arrival",
        "key_field_value": "Arriving in: 3 Minutes",
        "prompt": "When is the next southbound train arriving according to the sign?",
        "expected_safety_entity": "3 Minutes",
        "bg_color": (20, 20, 25),
        "text_color": (255, 180, 40)
    },
    {
        "id": "scene_07",
        "category": "scene_text",
        "title": "Chemistry Reagent Storage Cabinet",
        "distance_cm": 35,
        "lines": [
            "HAZARDOUS MATERIALS STORAGE CABINET",
            "FLAMMABLE LIQUIDS - CLASS 3",
            "NO SMOKING OR OPEN FLAME WITHIN 25 FT",
            "EMERGENCY EYEWASH STATION LOCATED AT LEFT"
        ],
        "key_field_type": "safety_class",
        "key_field_value": "Flammable Liquids - Class 3",
        "prompt": "What hazardous material classification is posted on this cabinet?",
        "expected_safety_entity": "Class 3",
        "bg_color": (230, 180, 20),
        "text_color": (20, 20, 20)
    },
    {
        "id": "scene_08",
        "category": "scene_text",
        "title": "University Library Quiet Floor Marker",
        "distance_cm": 38,
        "lines": [
            "CENTRAL UNIVERSITY LIBRARY - FLOOR 4",
            "SILENT STUDY ZONE - NO CELL PHONES",
            "PLEASE SET ALL DEVICES TO MUTE",
            "ASSISTANCE DESK AT ELEVATOR LOBBY"
        ],
        "key_field_type": "zone_rule",
        "key_field_value": "Silent Study Zone - No Cell Phones",
        "prompt": "What are the conduct rules for this library floor?",
        "expected_safety_entity": "Silent Study Zone",
        "bg_color": (245, 240, 235),
        "text_color": (40, 30, 25)
    },
    {
        "id": "scene_09",
        "category": "scene_text",
        "title": "Robotics Lab Warning Beacon",
        "distance_cm": 40,
        "lines": [
            "AUTONOMOUS MOBILE ROBOT TESTING AREA",
            "MAX VEHICLE SPEED: 1.5 M/S",
            "AUTHORIZED PERSONNEL ONLY PAST THIS POINT",
            "EMERGENCY E-STOP BUTTONS LOCATED ON ALL WALLS"
        ],
        "key_field_type": "speed_limit",
        "key_field_value": "Max Speed: 1.5 m/s",
        "prompt": "What is the maximum allowed vehicle speed in this testing area?",
        "expected_safety_entity": "1.5 m/s",
        "bg_color": (240, 230, 60),
        "text_color": (15, 15, 15)
    },
    {
        "id": "scene_10",
        "category": "scene_text",
        "title": "Modern Building Directory Entrance",
        "distance_cm": 40,
        "lines": [
            "NEXUS TOWER COMPLEX - BUILDING A",
            "FLOORS 1-3: NMIMS ENGINEERING LABS",
            "FLOORS 4-6: AI RESEARCH INCUBATOR",
            "VISITOR CHECK-IN AT DESK IN LOBBY",
            "SECURITY BADGE REQUIRED BEYOND TURNSTILES"
        ],
        "key_field_type": "facility_floor",
        "key_field_value": "Floors 4-6: AI Research Incubator",
        "prompt": "Which floors house the AI Research Incubator?",
        "expected_safety_entity": "Floors 4-6",
        "bg_color": (230, 235, 240),
        "text_color": (20, 30, 45)
    }
]

DEFAULT_PINNED_FONT_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "assets", "fonts", "DejaVuSansMono.ttf"
)

def render_photographic_benchmark_sample(spec, output_path, use_spec_font=False, font_path=None, font_size=21):
    """
    Renders photographic benchmark sample.
    - use_spec_font=False: Original 768x480 default bitmap font (stress set)
    - use_spec_font=True: 1536x960 TrueType font at 12.8 +/- 1 px/char (spec set, IMX415 camera optical spec)
    """
    font = None
    measured_px_per_char = 5.5
    
    if use_spec_font:
        fpath = font_path or DEFAULT_PINNED_FONT_PATH
        if not os.path.exists(fpath):
            raise FileNotFoundError(f"Pinned font not found at {fpath}")
        font = ImageFont.truetype(fpath, font_size)
        w, h = 1536, 960
    else:
        w, h = 768, 480

    bg = spec.get("bg_color", (245, 245, 242))
    fg = spec.get("text_color", (20, 20, 20))
    
    img = Image.new("RGB", (w, h), color=bg)
    draw = ImageDraw.Draw(img)

    # Add realistic photographic framing / ambient gradient
    for y in range(h):
        dist_from_center = abs(y - h/2) / (h/2)
        dim = int(dist_from_center * 12)
        r = max(0, bg[0] - dim)
        g = max(0, bg[1] - dim)
        b = max(0, bg[2] - dim)
        draw.line([(0, y), (w, y)], fill=(r, g, b))

    # Inner plaque / paper margin with soft shadow
    if use_spec_font:
        draw.rectangle([50, 50, w - 50, h - 50], outline=(180, 180, 180), width=4)
        draw.rectangle([46, 46, w - 46, h - 46], outline=(210, 210, 210), width=2)
    else:
        draw.rectangle([25, 25, w - 25, h - 25], outline=(180, 180, 180), width=2)
        draw.rectangle([23, 23, w - 23, h - 23], outline=(210, 210, 210), width=1)

    # Draw header bar if medicine or signage
    if use_spec_font:
        if spec["category"] == "medicine":
            draw.rectangle([54, 54, w - 54, 170], fill=(200, 30, 40))
            draw.text((90, 95), spec["lines"][0], font=font, fill=(255, 255, 255))
            y_start = 220
            body_lines = spec["lines"][1:]
        elif spec["category"] == "signage_menu":
            draw.rectangle([54, 54, w - 54, 160], fill=(30, 50, 80))
            draw.text((90, 85), spec["lines"][0], font=font, fill=(255, 255, 255))
            y_start = 210
            body_lines = spec["lines"][1:]
        else:
            y_start = 110
            body_lines = spec["lines"]

        y = y_start
        for i, line in enumerate(body_lines):
            if spec["category"] == "medicine" and i == 2:
                draw.rectangle([80, y - 8, w - 80, y + 45], fill=(235, 235, 230))
                draw.text((90, y), line, font=font, fill=(0, 0, 0))
                y += 76
            else:
                draw.text((90, y), line, font=font, fill=fg)
                y += 68

        # Measure textbbox dimensions and log average px/char per image
        all_line_widths = []
        all_line_chars = []
        for line in spec["lines"]:
            if not line:
                continue
            bbox = draw.textbbox((0, 0), line, font=font)
            all_line_widths.append(bbox[2] - bbox[0])
            all_line_chars.append(len(line))
        if all_line_chars and sum(all_line_chars) > 0:
            measured_px_per_char = sum(all_line_widths) / sum(all_line_chars)
        else:
            measured_px_per_char = float(font_size)

        # Apply realistic lens response
        img = img.filter(ImageFilter.GaussianBlur(radius=0.4))
    else:
        if spec["category"] == "medicine":
            draw.rectangle([27, 27, w - 27, 85], fill=(200, 30, 40))
            draw.text((45, 45), spec["lines"][0], fill=(255, 255, 255))
            y_start = 110
            body_lines = spec["lines"][1:]
        elif spec["category"] == "signage_menu":
            draw.rectangle([27, 27, w - 27, 80], fill=(30, 50, 80))
            draw.text((45, 42), spec["lines"][0], fill=(255, 255, 255))
            y_start = 105
            body_lines = spec["lines"][1:]
        else:
            y_start = 55
            body_lines = spec["lines"]

        y = y_start
        for i, line in enumerate(body_lines):
            if spec["category"] == "medicine" and i == 2:
                draw.rectangle([40, y - 4, w - 40, y + 26], fill=(235, 235, 230))
                draw.text((45, y), line, fill=(0, 0, 0))
                y += 38
            else:
                draw.text((45, y), line, fill=fg)
                y += 34

        img = img.filter(ImageFilter.GaussianBlur(radius=0.4))

    img.save(output_path, quality=95)
    return output_path, measured_px_per_char

def build_benchmark_suite(output_dir="assets/benchmark_dataset", use_spec_font=False, font_size=21):
    images_dir = os.path.join(output_dir, "images")
    os.makedirs(images_dir, exist_ok=True)
    manifest = []

    # Load required_fields from canonical existing manifest if available to guarantee exact parity
    existing_manifest_path = "assets/benchmark_dataset/benchmark_manifest.json"
    req_fields_map = {}
    if os.path.exists(existing_manifest_path):
        with open(existing_manifest_path) as f:
            for item in json.load(f):
                if "required_fields" in item:
                    req_fields_map[item["id"]] = item["required_fields"]

    mode_label = "Spec Resolution (12.8 px/char)" if use_spec_font else "Default Bitmap Resolution (Stress Set)"
    print(f"[*] Building 40-Sample Multimodal Benchmark Dataset ({mode_label}) in {output_dir}...")
    
    logged_px_chars = []
    for idx, spec in enumerate(BENCHMARK_SPECS):
        fname = f"{spec['id']}_{spec['category']}.jpg"
        fpath = os.path.join(images_dir, fname)
        _, px_per_char = render_photographic_benchmark_sample(
            spec, fpath, use_spec_font=use_spec_font, font_size=font_size
        )
        logged_px_chars.append(px_per_char)

        # Full ground truth preserving exact punctuation and whitespace
        full_gt = " ".join(spec["lines"])

        entry = {
            "id": spec["id"],
            "filename": fname,
            "category": spec["category"],
            "title": spec["title"],
            "distance_cm": spec["distance_cm"],
            "focus_quality": spec.get("focus_quality", "in_focus"),
            "ground_truth_full_text": full_gt,
            "key_field_type": spec["key_field_type"],
            "key_field_value": spec["key_field_value"],
            "prompt": spec["prompt"],
            "expected_safety_entity": spec["expected_safety_entity"]
        }
        if spec["id"] in req_fields_map:
            entry["required_fields"] = req_fields_map[spec["id"]]
        manifest.append(entry)
        print(f"  [{idx+1:02d}/40] [{spec['category']:12s}] {spec['title']:36s} [px/char: {px_per_char:.2f}] -> {fpath}")

    manifest_path = os.path.join(output_dir, "benchmark_manifest.json")
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

    # Compute manifest sha256
    import hashlib
    with open(manifest_path, "rb") as f:
        m_sha = hashlib.sha256(f.read()).hexdigest()
    sha_path = os.path.join(output_dir, "benchmark_manifest.sha256")
    with open(sha_path, "w") as f:
        f.write(f"{m_sha}  benchmark_manifest.json\n")

    # Auditor Item G2: Generate per-image sha256 mapping
    img_hashes = {}
    for entry in manifest:
        fn = entry["filename"]
        img_p = os.path.join(img_dir, fn)
        with open(img_p, "rb") as f:
            img_hashes[fn] = hashlib.sha256(f.read()).hexdigest()
    img_hashes_path = os.path.join(output_dir, "images_sha256.json")
    with open(img_hashes_path, "w") as f:
        json.dump(img_hashes, f, indent=2)

    avg_px = sum(logged_px_chars) / len(logged_px_chars)
    print(f"\n[✓] Benchmark Suite Successfully Compiled: {manifest_path}")
    print(f"    Manifest SHA256: {m_sha}")
    print(f"    Measured Average Resolution: {avg_px:.2f} px/char (Target: 12.8 +/- 1.0 px/char)\n")
    return manifest

if __name__ == "__main__":
    import sys
    if "--spec" in sys.argv:
        build_benchmark_suite("assets/benchmark_dataset_spec", use_spec_font=True)
    else:
        build_benchmark_suite()
