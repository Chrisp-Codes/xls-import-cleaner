# XLS Import Cleaner (Proof of Concept)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Status](https://img.shields.io/badge/status-POC-orange)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
[![English](https://img.shields.io/badge/README-English-informational?style=flat-square)](README_en.md)
[![Deutsch](https://img.shields.io/badge/README-Deutsch-informational?style=flat-square)](README.md)

## Problem Statement

When re-importing Excel files into HR systems (e.g., to update employee data), there is a risk of unintentionally overwriting or deleting existing records. The manual cleaning process before import is error-prone and time-consuming.

## Objective

This tool aims to automate the data cleaning process to prevent errors and save time. It is a technical proof of concept (PoC) to validate the proposed approach.

## Functionality

- Opens `.xls` / `.xlsx` files
- Clears or removes predefined cells, columns, or rows
- Saves a cleaned copy of the file for further processing

## Tests

This project uses [pytest](https://docs.pytest.org/) for automated testing.

### Running the tests (locally)

```bash
pip install -r requirements.txt
pytest
```

### Covered by tests:

- ✅ Successful cleaning run with example file  
- ❌ Proper error handling if “Personalnummer” is missing  
- 📝 More tests planned

All tests run automatically on each push via [GitHub Actions](https://github.com/Chrisp-Codes/xls-import-cleaner/actions).

## Status

- Not intended for production use
- Developed and tested with anonymized sample/test data
- Solely for technical demonstration

## Technologies

- Python 3.x
- openpyxl (Excel processing)
- tkinter (GUI)
- Optional: pyinstaller (for generating an executable)

## Compiling as `.exe` (optional)

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole src/gui.py
```
