import os
import shutil
from src.gui import clean_import_file

def test_clean_import_creates_file(tmp_path):
    # Pfad zur bestehenden Dummy-Datei
    source_file = "dummy_import.xlsx"
    
    # Zielpfad im temporären Testordner
    test_file = tmp_path / "test.xlsx"
    shutil.copy(source_file, test_file)

    # Funktion ausführen
    result_file = clean_import_file(str(test_file), mode="startdaten")

    # Prüfen ob Datei erstellt wurde
    assert os.path.exists(result_file)
    assert "_bereinigt" in result_file
