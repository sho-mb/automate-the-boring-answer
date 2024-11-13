#!/usr/bin/env python3
# toText.py

import os
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

textFile = 'readMe.txt'

absWorkingDir = os.path.abspath('.')
target = os.path.join(absWorkingDir, textFile)

print("Text file path:", target)

with open(target, 'r') as readFile:
    textContent = readFile.readlines()

for row, line in enumerate(textContent, start=1):
    sheet.cell(row=row, column=1).value = line.strip()

wb.save('convertedText.xlsx')

print("Text content has been written to 'convertedText.xlsx'")
