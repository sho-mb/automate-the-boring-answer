
import re

whiteSpaceRegix = re.compile(r'^\s+|\s$')

def strip(s, chars=None):
    if chars is None:
        return whiteSpaceRegix.sub('',s)
    else:
        pattern = '^[' + re.escape(chars) + ']+|[' + re.escape(chars) + ']+$'
        return re.compile(pattern).sub('', s)
        

result = strip('hello world', 'held')
print(result)
    
