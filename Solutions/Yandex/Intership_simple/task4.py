import sys
from typing import List

def generate(n: int, left: int, right: int, path: List):
    
    if left + right == 2*n:
        print(''.join(path))
        return
    
    if left < n:
        path.append('(')
        generate(n, left+1, right, path)
        path.pop()
        
    if right < n and right < left:
            path.append(')')
            generate(n, left, right+1, path)
            path.pop()
            

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    generate(n, 0, 0, [])

if __name__ == '__main__':
    solve()