#MadLibs.py

import re, os

file_path = '/users/kisho/downloads/text.txt'

if os.path.exists(file_path):
    textFile = open(file_path, 'r')
    readText = textFile.read()
    print(readText)
    textFile.close() 

    adjectiveRegix = re.compile(r'\bADJECTIVE\b')
    nuouRegix = re.compile(r'\bNOUN\b')
    verbRegix = re.compile(r'\bVERB\b')
    adverbRegix = re.compile(r'\bADVERB\b')

    print('Enter an adjective:')
    adjective = input()
    readText = adjectiveRegix.sub(adjective, readText)
    print(readText)

    print('Enter a noun:')
    noun = input()
    readText =  nuouRegix.sub(noun, readText)
    print(readText)

    print('Enter a verb:')
    verb = input()
    readText =  verbRegix.sub(verb, readText)
    print(readText)

    print('Enter a adverb')
    adverb = input()
    readText = adverbRegix.sub(adverb, readText)
    print(readText)

    new_file_path = '/users/kisho/downloads/text_modified.txt'
    newFile = open(new_file_path, 'w')
    newFile.write(readText)
    newFile.close()
else:
    print('Not exist this path')
