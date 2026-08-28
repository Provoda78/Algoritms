import sys
from typing import List

def counter_chars(s: str)->str:
    if not s:
        return ''
    
    s += '*'
    res = []
    
    prev = s[0]
    counter = 0
    for ch in s:
        if prev == ch:
            counter += 1
        else:
            res.append(f"{prev}{counter}" if counter > 1 else prev)
            prev = ch
            counter = 1    
            
    return ''.join(res)    
            
            