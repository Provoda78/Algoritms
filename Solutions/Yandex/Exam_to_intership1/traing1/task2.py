import sys

def solve():
    raw_input = sys.stdin.read()
    if not raw_input:
        return 0

    s = raw_input.rstrip('\r\n')
        
    max_len = 0
    start = 0
    char_index = {}
    
    for idx, chr in enumerate(s):
        
        if chr in char_index and char_index[chr] >= start:
            start = char_index[chr] + 1
        
        char_index[chr] = idx
        
        if idx - start + 1 > max_len:
            max_len = idx - start + 1
    
    return max_len

if __name__ == '__main__':
    ans = solve()
    print(ans)