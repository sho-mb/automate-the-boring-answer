#! /usr/bin/env python3
#unneededFiles.py

import os

absWorkingDir = os.path.abspath('.')
print('Check dir of ' + absWorkingDir)
for foldername, subfolders, filenames in os.walk(absWorkingDir):        
    for filename in filenames:
        fileSize = os.path.getsize(os.path.join(foldername, filename))
        if fileSize >= 1048576:
            print('Found learge file in: ' + foldername + ': ' + filename + 'size is: ' + str(round(fileSize / 1048576)) + 'MB')
            print('')

    
