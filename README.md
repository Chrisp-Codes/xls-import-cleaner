[English Version](README_en.md)

# XLS Import Cleaner (POC)

## Überblick
Dieses Repository enthält ein Proof of Concept für ein kleines Python-Tool zur automatisierten Bereinigung von Excel-Importdateien.  
Ziel ist es, den manuellen Aufwand beim "Clearing" vor Re-Imports zu reduzieren und potenzielle Fehlerquellen zu minimieren.

## Funktionsweise
- Öffnet eine XLS/XLSX-Datei
- Leert definierte Zellen/Spalten/Zeilen
- Speichert die Datei als neue Version ab

## Motivation
Der manuelle Clearing-Prozess ist zeitaufwendig und fehleranfällig. Dieses Tool dient als Machbarkeitsstudie (Proof of Concept), um zu zeigen, wie sich der Prozess automatisieren lässt.

## Status
- Aktuell nur als private Demo entwickelt
- Nicht für den produktiven Einsatz freigegeben
- Getestet mit Beispiel- und Testdaten

## Technologien
- Python
- OpenPyXL
- Tkinter

## Hinweis
Dies ist ein **POC** und nicht offiziell freigegeben. Nutzung erfolgt auf eigene Verantwortung.


## Deployment (optional)

Das Tool kann bei Bedarf zu einer eigenständigen `.exe` kompiliert werden:

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole src/gui.py
