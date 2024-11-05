spam = ['apples', 'bananas', 'tofu', 'cats', 'apples', 'bananas', 'tofu', 'cats', 'apples', 'bananas', 'tofu', 'cats']

def listToString(list):
    converted = ''
    for i in range(len(list)):
        if i == 0:
            item = "'" + list[i] + ', '
            converted += item
        elif i == len(list) - 1:
            item = 'and ' + list[i] + "'"
            converted += item
        else:
            item = list[i] + ', '
            converted += item
    return converted

convertedString = listToString(spam)
print(convertedString)
