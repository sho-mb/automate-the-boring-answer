#! /usr/bin/env python3
#regixSearch.py folderpath

import sys, re, os

if len(sys.argv) == 2:
    if os.path.exists(sys.argv[1]):
        folder_path = sys.argv[1]
        files = os.listdir(folder_path)

        #pattern = re.compile(sys.argv[2])
        print('Please enter Regix: ')
        regix = input()
        pattern = re.compile(regix)

        for file in files:
            if file.endswith('.txt'):
                print('----' + file + '----')
                path = os.path.join(folder_path, file)
                
                txtFile = open(path, 'r')
                readText = txtFile.read()
                txtFile.close()

                matches = pattern.findall(readText)
                if len(matches) > 0:
                    for match in matches:
                        print(''.join(match))
    else:
        print('Invalid path')
else:
    print('Please input folder path ./regixSearch.py /dirName ')
