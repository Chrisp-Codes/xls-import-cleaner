# XLS Import Cleaner (Proof of Concept)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/status-POC-orange)
![Made with ❤️](https://img.shields.io/badge/made%20with-%E2%9D%A4-red)
![Tests](https://github.com/Chrisp-Codes/xls-import-cleaner/actions/workflows/python-tests.yml/badge.svg)


[English Version](README_en.md)

## Problemstellung

Beim Re-Import von Excel-Dateien in HR-Systeme (zum Beispiel zur Aktualisierung von Mitarbeiterdaten) besteht die Gefahr, dass unbeabsichtigt bestehende Datensätze überschrieben oder gelöscht werden. Der manuelle Bereinigungsprozess vor dem Import ist fehleranfällig und zeitaufwendig.

## Zielsetzung

Dieses Tool soll den Prozess der Datenbereinigung automatisieren, um Fehler zu vermeiden und Zeit zu sparen. Es handelt sich um eine technische Machbarkeitsstudie (Proof of Concept) zur Validierung des Lösungsansatzes.

## Funktionsweise

- Öffnet `.xls` / `.xlsx`-Dateien
- Leert oder entfernt vordefinierte Zellen, Spalten oder Zeilen
- Speichert eine bereinigte Kopie der Datei zur Weiterverarbeitung

## Status

- Nicht für den produktiven Einsatz vorgesehen
- Entwickelt und getestet mit anonymisierten Beispiel- und Testdaten
- Dient ausschließlich der technischen Demonstration

## Technologien

- Python 3.x
- openpyxl (Excel-Dateiverarbeitung)
- tkinter (GUI)
- Optional: pyinstaller (für die Erstellung einer ausführbaren Datei)

## Kompilierung als `.exe` (optional)

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole src/gui.py
