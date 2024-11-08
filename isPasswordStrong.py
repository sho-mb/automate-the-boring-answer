#strong password

#conditions: at least eight characters long, OK
#contains both uppercase and lowercase characters,
#and has at least one digit.

import re

passwords = ['aa','aaaaaaaaa','aaaaaAAAA','aaa123AAA']


def isStrongPassword(pw):
    if len(pw) < 8:
        return False

    if not re.compile(r'[A-Z]').search(pw):
        return False

    if not re.compile(r'[a-z]').search(pw):
        return False

    if not re.compile(r'[0-9]').search(pw):
        return False

    return True

for i in range(len(passwords)):
    if (isStrongPassword(passwords[i])):
        print('Strong!')
    else:
        print('Week...')
