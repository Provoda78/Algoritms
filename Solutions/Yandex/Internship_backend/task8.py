import sys

def solve():
    s = sys.stdin.read().strip()
    if not s:
        print('yes')
        return
    
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}
    
    for ch in s:
        if ch in matching:
            if not stack or matching[ch] != stack[-1]:
                print('no')
                return
            stack.pop()
        else:
            stack.append(ch)
            
    if not stack:
        print('yes')
    else:
        print('no')
        
if __name__ == '__main__':
    solve()