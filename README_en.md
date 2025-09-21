# XLS Import Cleaner (POC)

## Overview
This repository contains a **proof of concept** for a small Python tool that automates the cleanup of Excel import files.  
The goal is to reduce the manual effort required for "clearing" before re-imports and to minimize potential errors.

## How It Works
- Opens an XLS/XLSX file  
- Clears specific cells/columns/rows based on defined rules  
- Saves the file as a new version with a modified name  

## Motivation
The manual clearing process is time-consuming and error-prone.  
This tool serves as a **proof of concept** to demonstrate how the process can be automated.

## Status
- Currently developed as a private demo  
- **Not intended for production use**  
- Tested only with example and test data  

## Technologies
- Python  
- OpenPyXL  
- Tkinter  

## Disclaimer
This is a **POC project** and not officially released. Use at your own risk.

## Deployment (optional)
The tool can be compiled into a standalone `.exe` if needed:

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole src/gui.py
