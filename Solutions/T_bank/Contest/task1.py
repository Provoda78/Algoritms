from typing import List

def solve(n: int, arr: List) -> str:
    
    arr.sort()
    
    if (all(num == arr[-1] for num in arr[2:])):
        if arr[0] + arr[1] == arr[-1]:
            print('YES')
            return
    
    print('NO')
    
if __name__ == '__main__':
    n = int(input())
    v = list(map(int, input().split()))
    
    solve(n, v)