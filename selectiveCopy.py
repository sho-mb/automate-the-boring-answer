#! /usr/bin/env python3
#selectiveCopy.py

import sys, os, shutil

if len(sys.argv) == 2:
    folder_path = sys.argv[1]
    if os.path.exists(folder_path):
        print('Please enter extention that you want to copy of: ')
        extention = input()

        absWorkingDir = os.path.abspath('.')
        copyPath = os.path.join(absWorkingDir, 'copy')
        if not os.path.exists(copyPath):
            os.mkdir(copyPath)
            
        for foldername, subfolders, filenames in os.walk(folder_path):
            print('The current folder is ' + foldername)
            
            for filename in filenames:
                if filename.endswith('.' + extention):
                    filePath = os.path.join(foldername, filename)
                    shutil.copy(filePath, copyPath), 
            print('')
    else:
        print('Invalid Path')
else:
    print('Please specify path: ./selectiveCopy.py pathname')
