#!/usr/bin/env python3
"""
generate_reference_notes.py
Generates documentation notes in docs/reference_designs/notes/ for Project FRIDAY.
"""

import os
import sys
import subprocess

def run_emcp_generator():
    script = os.path.join(os.path.dirname(__file__), 'extract_emcp_ballmap.py')
    subprocess.run([sys.executable, script], check=True)

if __name__ == '__main__':
    run_emcp_generator()
    print('All reference notes generated.')
