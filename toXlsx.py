#!/usr/bin/env python3
# toText.py

import os
import openpyxl

excelFile = 'readMe.xlsx'

wb = openpyxl.load_workbook(excelFile)
sheet = wb.active

textFile = 'readMe.txt'

absWorkingDir = os.path.abspath('.')
target = os.path.join(absWorkingDir, textFile)

print("Writing data to text file at:", target)

with open(target, 'w') as writeFile:
    for row in sheet.iter_rows(values_only=True):
        line = "\t".join([str(cell) if cell is not None else "" for cell in row])
        writeFile.write(line + '\n') 

print("Excel content has been written to", textFile)
