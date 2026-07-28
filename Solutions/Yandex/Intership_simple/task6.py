import sys
from typing import List

def solve():
    input_data = sys.stdin.read().split()
    
    n = int(input_data[0])
    
    proud = float('inf')
    
    for i in range(1, n+1):
        
        num = input_data[i] 
        if num != proud:
            print(num)
            proud = num


if __name__ == '__main__':
    solve()