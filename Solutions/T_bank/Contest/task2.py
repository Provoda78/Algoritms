import sys
from typing import List
from collections import Counter

def solve(n: int, arr: List[str]) -> None:
    
    counts = Counter(arr)
    max_freq = max(list(counts.values()))
    
    res = [word for word, f in counts.items() if f == max_freq]
    
    res.sort()
    
    for w in res:
        print(w)
        
if __name__ == '__main__':
    input_d = sys.stdin.read().split()
    
    n = int(input_d[0])
    words = input_d[1:]
    
    solve(n, words)