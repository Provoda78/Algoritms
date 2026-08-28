from typing import List

def solve(arr: List[int], n: int, q: int) -> List[str]:
    res = []
    
    prev = [0] * (n+1)
    pref = [0] * (n+1)
    visited = {}
    
    for i in range(1, n+1):
        num = arr[i]
        
        if num in visited:
            prev[i] = visited[num]
        
        visited[num] = i
            
    for i in range(1, len(prev)):
        pref[i] = max(pref[i-1], prev[i])
            
    for _ in range(q):
        l, r = list(map(int, input().split()))
        
        res.append('YES' if pref[r] >= l else 'NO')
    
    return res