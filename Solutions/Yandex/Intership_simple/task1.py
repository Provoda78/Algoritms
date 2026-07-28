import sys

def solve():
    lines = sys.stdin.read().splitlines()
    
    j = set(lines[0]) if len(lines) > 0 else set()
    s = lines[1] if len(lines) > 1 else ""
    
    ans = sum(1 for char in s if char in j)
    
    print(ans)

if __name__ == '__main__':
    solve()