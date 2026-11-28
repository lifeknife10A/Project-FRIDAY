"""Run inside Fusion to export the generated SCH-4a schematic and its ERC results."""

import json
from pathlib import Path

import adsk
import adsk.core
import adsk.electron


def run(_context):
    board_directory = Path(__file__).resolve().parent
    source = board_directory / "FRIDAY_Left_SCH4a.sch"
    export_directory = Path("/tmp/friday-sch4a-fusion")
    export_directory.mkdir(exist_ok=True)
    application = adsk.core.Application.get()
    if adsk.electron.Schematic.cast(application.activeProduct) is None:
        application.userInterface.commandDefinitions.itemById("NewElectronSchDocumentCommand").execute()
        adsk.doEvents()
    application.executeTextCommand(f"Electron.run EDIT '{source}';")
    document = application.activeDocument
    schematic = adsk.electron.Schematic.cast(application.activeProduct)
    if schematic is None or document.name not in (source.name, source.stem):
        raise RuntimeError(f"Expected the imported SCH-4a schematic, found {document.name}")

    export_manager = schematic.exportManager
    options = export_manager.createEagleSchExportOptions(str(export_directory / source.name))
    if not export_manager.execute(options):
        raise RuntimeError("Fusion schematic export failed")
    netlist_path = export_directory / f"{source.stem}_netlist.txt"
    pdf_path = export_directory / "SCH-4a.pdf"
    for path in (netlist_path, pdf_path):
        path.unlink(missing_ok=True)
    for command in (
        f"EXPORT NETLIST '{netlist_path}';",
        "DISPLAY 95 96 -93;",
        f"PRINT 1 -1 PAPER A3 LANDSCAPE SHEETS ALL FILE '{pdf_path}';",
        "ERC;",
    ):
        application.executeTextCommand(f"Electron.run {command}")

    results = {
        "document": document.name,
        "fusion": application.version,
        "checked": schematic.checked,
        "issues": [
            {"code": issue.code, "type": issue.errorType, "state": issue.state,
             "sheet": issue.sheet, "signature": issue.signature, "description": issue.description}
            for issue in schematic.errors
        ],
    }
    (export_directory / "erc.json").write_text(json.dumps(results, indent=2), encoding="utf-8")
    if application.userInterface.activeCommand.startswith("Electron::"):
        application.userInterface.terminateActiveCommand()
    if not schematic.checked or not netlist_path.is_file() or not pdf_path.is_file():
        raise RuntimeError("Fusion did not return all SCH-4a outputs")
    print(f"Fusion {application.version}: {schematic.sheets.count} sheets, ERC checked, "
          f"{len(results['issues'])} ERC entries. Exports in {export_directory}.")
