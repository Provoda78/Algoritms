import sys

def solve():
    
    s1 = input()
    s2 = input()
    
    print(int(sorted(s1) == sorted(s2)))
    
if __name__ == '__main__':
    solve()