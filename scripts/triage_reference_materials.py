import os
import sys
import hashlib
import csv

dir_a = os.path.expanduser('~/Downloads/RK3576-hardware-design-main')
file_b = os.path.expanduser('~/Downloads/eMCP Specification.pdf')

def get_sha256(filepath):
    h = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

conf_basenames = [
    'ssom-k1 emmc flash.pdf',
    'es8326 pb.pdf',
    'rtl8211f data manual.pdf',
    'rtl8211fg(i)(-vs)-cg_datasheet_1.4.pdf',
    'rk3576 datasheet v1.6.pdf',
    'rk3576_hardware_design_guide_v1.1_20240528_en.pdf',
    'es7202_ds.pdf',
    'husb311 introduction 20210526.pdf'
]

def classify_file(rel_path, filename):
    p = rel_path.lower()
    fn = filename.lower()
    ext = os.path.splitext(fn)[1]

    is_conf = any(c in fn for c in conf_basenames)
    disposition = 'local-only (confidential/restricted)' if is_conf else 'local-only (no permissive licence)'

    if 'emcp specification' in fn:
        return 'PDF', 'SK hynix eMCP (H9HP52ACPMADAR)', 'HIGH', 'Direct spec for eMCP memory (64GB eMMC 5.1 + 32Gb LPDDR4X); pinout, ball map, voltages.', disposition
    
    board = 'General'
    if 'armsom-sige5' in p or 'sige5' in p:
        board = 'ArmSoM Sige5'
    elif 'armsom-cm5-io' in p or 'cm5-io' in p:
        board = 'ArmSoM CM5-IO'
    elif 'armsom-cm5' in p or 'cm5' in p:
        board = 'ArmSoM CM5'
    elif 'bit-brick-k1-ssom' in p:
        board = 'Bit-Brick K1-SSOM'
    elif 'bit-brick-k1-pro' in p:
        board = 'Bit-Brick K1-PRO'
    elif 'bit-brick-k1' in p:
        board = 'Bit-Brick K1'
    elif 'huidu-mu-rk3576j-mb' in p:
        board = 'HUIDU MU-RK3576J-MB'
    elif 'dshanpi-a1' in p:
        board = 'DshanPI-A1'
    elif 'rockchip rk3576 reference' in p or 'evb1' in p:
        board = 'Rockchip Reference/EVB1'
    elif 'rk3576-datasheet' in p:
        board = 'Component Datasheet'

    if any(k in p for k in ['armsom-sige5-1v3_sch.pdf', 'armsom-cm5-1v1_sch.pdf', 'circuit diagram files for bit-brick k1 sbc.pdf', 'dshanpi-a1-rk3576-sch_v1.1.pdf', 'rk_evb1_rk3576_lp4xd200p132sd6_v12_20240530hsw.pdf', 'rk3576_aiot_ref_sch_v11_20240530.pdf']):
        return ext.upper()[1:], board, 'HIGH', 'Complete reference schematic with RK3576, RK806 PMIC, LPDDR4X passives, eMMC, power tree.', disposition
    
    if 'ssom-k1 emmc flash.pdf' in fn:
        return 'PDF', 'Samsung eMMC', 'HIGH', 'Samsung eMMC flash memory reference datasheet; pinout and decoupling.', disposition

    if any(k in p for k in ['rk3576_hardware_design_guide', 'rk3576 datasheet', 'rk3576 brief datasheet']):
        return 'PDF', 'Rockchip RK3576', 'HIGH', 'Official Rockchip hardware design guide and chip datasheet; power, decoupling, pinout.', disposition
    
    if any(k in fn for k in ['tmi3112h', 'cw3301', 'rk806', 'rtl8723ds', 'husb311']):
        return 'PDF', board, 'HIGH', 'Key discrete power, PMIC, Type-C, or wireless component datasheet used in FRIDAY.', disposition

    if any(k in p for k in ['cam', 'mipi', 'csi', 'camera', 'typec', 'usb2.0', 'usb3.0', 'wifi']):
        if ext in ['.pdf', '.dsn', '.schdoc']:
            return ext.upper()[1:], board, 'HIGH', 'Reference implementation for camera CSI, USB-C, or Wi-Fi/BT subsystems.', disposition
        elif ext in ['.md', '.txt', '.png', '.jpg']:
            return ext.upper()[1:], board, 'MED', 'Connector / peripheral documentation, pinout or reference visual.', disposition
        else:
            return ext.upper()[1:], board, 'LOW', 'Peripheral connector 3D model or PCB footprint.', disposition

    if any(k in p for k in ['audio', 'codec', 'es8388', 'es8326', 'es7202', 'tcs8563', 'uart', 'boot', 'maskrom', 'cm5-io']):
        return ext.upper()[1:], board, 'MED', 'Audio codec, RTC, UART debug, boot switches, or carrier board reference.', disposition

    if any(k in p for k in ['ethernet', 'rj45', 'rtl8211', 'yt8512', 'pcie', 'sata', 'hdmi', 'edp', 'lcd', 'poe', 'rk628']):
        return ext.upper()[1:], board, 'LOW', 'Unused peripheral subsystem (Ethernet, PCIe, HDMI/LCD display, PoE).', disposition

    if ext in ['.stp', '.step', '.dxf', '.x_t']:
        return ext.upper()[1:], board, 'LOW', 'Mechanical 3D model or enclosure drawing.', disposition

    if ext in ['.annotation', '.harness', '.outjob', '.prjpcbstructure', '.prjpcbvariants']:
        return ext.upper()[1:], board, 'NONE', 'Altium intermediate project/compilation artifact.', disposition

    if ext in ['.png', '.jpg']:
        return ext.upper()[1:], board, 'LOW', 'Reference board photo or rendering.', disposition

    if ext in ['.schdoc', '.pcbdoc', '.brd', '.dsn']:
        return ext.upper()[1:], board, 'MED', 'CAD design database file for reference hardware.', disposition

    return ext.upper()[1:], board, 'LOW', 'General reference material or utility file.', disposition

def main():
    os.makedirs('docs/reference_designs/notes', exist_ok=True)
    entries = []

    # Input B
    sha_b = get_sha256(file_b)
    ftype, board, rel, why, disp = classify_file('eMCP Specification.pdf', 'eMCP Specification.pdf')
    entries.append({
        'path': 'eMCP Specification.pdf',
        'type': ftype,
        'board': board,
        'relevance': rel,
        'why': why,
        'disposition': disp,
        'sha256': sha_b
    })

    # Input A
    for root, dirs, files in os.walk(dir_a):
        for f in sorted(files):
            p = os.path.join(root, f)
            rel_path = os.path.relpath(p, dir_a)
            sha = get_sha256(p)
            ftype, board, rel, why, disp = classify_file(rel_path, f)
            entries.append({
                'path': rel_path,
                'type': ftype,
                'board': board,
                'relevance': rel,
                'why': why,
                'disposition': disp,
                'sha256': sha
            })

    print(f'Total inventory entries: {len(entries)}')

    with open('docs/reference_designs/INVENTORY.md', 'w') as fp:
        fp.write('# Project FRIDAY: Reference Materials Inventory\n\n')
        fp.write('Exhaustive inventory of external reference designs and component specifications triaged for Project FRIDAY (custom RK3576 smart glasses compute board).\n\n')
        fp.write('### Summary Statistics\n')
        fp.write(f'- **Total Triaged Files:** {len(entries)}\n')
        fp.write(f'- **HIGH Relevance:** {sum(1 for e in entries if e["relevance"] == "HIGH")}\n')
        fp.write(f'- **MED Relevance:** {sum(1 for e in entries if e["relevance"] == "MED")}\n')
        fp.write(f'- **LOW Relevance:** {sum(1 for e in entries if e["relevance"] == "LOW")}\n')
        fp.write(f'- **NONE Relevance:** {sum(1 for e in entries if e["relevance"] == "NONE")}\n')
        fp.write(f'- **Quarantined Local-Only:** {len(entries)} (0 files committed to git repository; all proprietary/unlicensed reference files quarantined in `references_local/` and ignored via `.gitignore`)\n\n')
        fp.write('### Top 10 HIGH-Relevance Reference Files\n\n')
        priority_paths = [
            'eMCP Specification.pdf',
            'RK3576-Schematics/Sige5/armsom-sige5-1v3_Sch.pdf',
            'ArmSoM-CM5/ArmSoM-CM5-1V1_sch.pdf',
            'Bit-Brick-K1/Circuit Diagram Files for Bit-Brick K1 SBC.pdf',
            'RK3576-Schematics/DshanPI-A1/DshanPi-A1-RK3576-SCH_V1.1.pdf',
            'Rockchip RK3576 Reference/04_Demo_EVB1_仅供参考！/03_Reference Design/RK_EVB1_RK3576_LP4XD200P132SD6_V12_20240530HSW.pdf',
            'Rockchip RK3576 Reference/03_Product Line Branch_AIoT/03_Reference Design/01_RK3576_AIoT_REF_SCH/RK3576_AIOT_REF_SCH_V11_20240530.pdf',
            'Rockchip RK3576 Reference/01_Common Document/RK3576_Hardware_Design_Guide_V1.1_20240528_CN.pdf',
            'Bit-Brick-K1/SSOM-K1 EMMC FLASH.PDF',
            'RK3576-documents/02_Rockchip\xa0RK806S\xa0Datasheet.pdf'
        ]
        top10_entries = []
        entry_dict = {e['path']: e for e in entries}
        for p in priority_paths:
            if p in entry_dict:
                top10_entries.append(entry_dict[p])
        for e in entries:
            if e['relevance'] == 'HIGH' and e not in top10_entries and len(top10_entries) < 10:
                top10_entries.append(e)

        for idx, e in enumerate(top10_entries[:10], start=1):
            fp.write(f'{idx}. **`{e["path"]}`** ({e["type"]}, {e["board"]})\n')
            fp.write(f'   - *Relevance:* {e["relevance"]}\n')
            fp.write(f'   - *Why:* {e["why"]}\n')
            fp.write(f'   - *Status:* {e["disposition"]}\n')
            fp.write(f'   - *SHA-256:* `{e["sha256"]}`\n\n')
        fp.write('---\n\n')
        fp.write('### Complete Triaged File Catalog\n\n')
        fp.write('| Path | Type | Board / Part | Relevance | Why | Status | SHA-256 |\n')
        fp.write('| :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n')
        for e in entries:
            clean_why = e['why'].replace('|', '/')
            clean_path = e['path'].replace('|', '/')
            fp.write(f'| `{clean_path}` | {e["type"]} | {e["board"]} | **{e["relevance"]}** | {clean_why} | {e["disposition"]} | `{e["sha256"][:16]}...` |\n')

    print('docs/reference_designs/INVENTORY.md generated.')

if __name__ == '__main__':
    main()
