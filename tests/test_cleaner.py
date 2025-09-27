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

def test_clean_import_raises_without_header(tmp_path):
    source_file = "dummy_no_header.xlsx"
    test_file = tmp_path / "broken.xlsx"
    shutil.copy(source_file, test_file)

    try:
        clean_import_file(str(test_file), mode="startdaten")
        assert False, "Fehler wurde nicht geworfen"
    except ValueError as e:
        assert "Personalnummer" in str(e)
