import sys

def solve():
    input_d = sys.stdin.read().split()
    if not input_d:
        return
    
    h = int(input_d[0])
    w = int(input_d[1])
    
    grid = input_d[2:]
    
    first_p = [float('inf')] * w
    for c in range(w):
        for r in range(h):
            if grid[r * w + c] == 'P':
                first_p[c] = r
                break
                
    takts = [1] * w
    max_time = 1
    
    for r in range(1, h):
        new_takts = [float('inf')] * w
        
        for c in range(w):
            if r - 1 >= first_p[c]:
                new_takts[c] = takts[c] + 1
                
        for c in range(1, w):
            if r >= first_p[c - 1]:
                if new_takts[c - 1] + 1 < new_takts[c]:
                    new_takts[c] = new_takts[c - 1] + 1
                    
        for c in range(w - 2, -1, -1):
            if r >= first_p[c + 1]:
                if new_takts[c + 1] + 1 < new_takts[c]:
                    new_takts[c] = new_takts[c + 1] + 1
        
        for c in range(w):
            if new_takts[c] > max_time:
                max_time = new_takts[c]
            takts[c] = new_takts[c]
            
    if max_time == float('inf'):
        print(-1)
    else:
        print(max_time)

if __name__ == '__main__':
    solve()