import os
import sys
import shutil

# src/ Verzeichnis zum Importpfad hinzufügen
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from gui import clean_import_file  # kein src. mehr nötig!

def test_clean_import_creates_file(tmp_path):
    source_file = "dummy_import.xlsx"
    test_file = tmp_path / "test.xlsx"
    shutil.copy(source_file, test_file)

    result_file = clean_import_file(str(test_file), mode="startdaten")

    assert os.path.exists(result_file)
    assert "_bereinigt" in result_file
