"""Run inside Fusion to export each SCH-4b schematic and its native ERC results."""

import json
from pathlib import Path

import adsk
import adsk.core
import adsk.electron


def export_board(application, source, board_label):
    export_directory = Path("/tmp/friday-sch4b-fusion") / board_label
    export_directory.mkdir(parents=True, exist_ok=True)
    if adsk.electron.Schematic.cast(application.activeProduct) is None:
        application.userInterface.commandDefinitions.itemById("NewElectronSchDocumentCommand").execute()
        adsk.doEvents()
    application.executeTextCommand(f"Electron.run EDIT '{source}';")
    document = application.activeDocument
    schematic = adsk.electron.Schematic.cast(application.activeProduct)
    if schematic is None or document.name not in (source.name, source.stem):
        raise RuntimeError(f"Expected {source.name}, found {document.name}")

    export_manager = schematic.exportManager
    options = export_manager.createEagleSchExportOptions(str(export_directory / source.name))
    if not export_manager.execute(options):
        raise RuntimeError("Fusion schematic export failed")
    netlist = export_directory / f"{source.stem}_netlist.txt"
    pdf = export_directory / f"SCH-4b_{board_label}.pdf"
    for path in (netlist, pdf):
        path.unlink(missing_ok=True)
    for command in (f"EXPORT NETLIST '{netlist}';", "DISPLAY 95 96 -93;",
                    f"PRINT 1 -1 PAPER A3 LANDSCAPE SHEETS ALL FILE '{pdf}';", "ERC;"):
        application.executeTextCommand(f"Electron.run {command}")
    result = {
        "document": document.name, "fusion": application.version, "checked": schematic.checked,
        "issues": [{"code": issue.code, "type": issue.errorType, "state": issue.state, "sheet": issue.sheet,
                    "signature": issue.signature, "description": issue.description}
                   for issue in schematic.errors],
    }
    (export_directory / "erc.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    if application.userInterface.activeCommand.startswith("Electron::"):
        application.userInterface.terminateActiveCommand()
    if not schematic.checked or not netlist.is_file() or not pdf.is_file():
        raise RuntimeError(f"Fusion did not return all {board_label} outputs")
    print(f"{board_label}: {schematic.sheets.count} sheets, {len(result['issues'])} native ERC entries.")


def run(context):
    directory = Path(__file__).resolve().parent
    application = adsk.core.Application.get()
    if context != "compute-only":
        export_board(application, directory.parent / "left_temple/FRIDAY_Left_SCH4b.sch", "Left")
    export_board(application, directory / "FRIDAY_Compute_SCH4b.sch", "Compute")
