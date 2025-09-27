# XLS Import Cleaner (Proof of Concept)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Status](https://img.shields.io/badge/status-POC-orange)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
[![English](https://img.shields.io/badge/README-English-informational?style=flat-square)](README_en.md)
[![Deutsch](https://img.shields.io/badge/README-Deutsch-informational?style=flat-square)](README.md)

## Problem Statement

When re-importing Excel files into HR systems (e.g. to update employee records), there is a significant risk of unintentionally overwriting or deleting existing data. Manual cleaning of import files prior to upload is time-consuming and prone to human error.

## Objective

This tool aims to automate the data cleaning process to reduce errors and save time. It serves as a technical proof of concept to validate the feasibility of such automation.

## Functionality

- Opens `.xls` / `.xlsx` files
- Clears or removes predefined cells, columns, or rows
- Saves a cleaned copy of the original file for further processing

## Project Status

- Not intended for production use
- Tested with anonymized sample and test data
- Built solely for technical demonstration purposes

## Technologies Used

- Python 3.x
- openpyxl (for Excel file handling)
- tkinter (for the GUI)
- Optional: pyinstaller (to create an executable)

## Optional: Build as `.exe`

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole src/gui.py
