# XLS Import Cleaner (Proof of Concept)
![Excel VBA](https://img.shields.io/badge/Microsoft%20Excel-VBA-green?logo=microsoft-excel&logoColor=white)
![Language](https://img.shields.io/badge/language-VBA-blue)
![Status](https://img.shields.io/badge/status-POC-orange)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
[![English](https://img.shields.io/badge/README-English-informational?style=flat-square)](README_en.md)
[![Deutsch](https://img.shields.io/badge/README-Deutsch-informational?style=flat-square)](README.md)



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
