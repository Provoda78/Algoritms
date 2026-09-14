import sys

def solve(n, t, cells):
    if not n or not t:
        return
    
    rows = [0] * n
    colms = [0] * n
    
    dig1, dig2 = 0, 0
    
    for i in range(t):
        
        cell = cells[i]
        r = cell // n
        c = cell % n
        
        rows[r] += 1
        if rows[r] == n:
            print(i+1)
            return
        
        colms[c] += 1
        if colms[c] == n:
            print(i+1)
            return
            
        if r == c:
            dig1 += 1
            if dig1 == n:
                print(i+1)
                return
        
        if r + c == n - 1:
            dig2 += 1
            if dig2 == n:
                print(i + 1)
                return
    print(-1)
    return

if __name__ == '__main__':
    
    input_d = sys.stdin.read().split()
    if input_d:
        n = int(input_d[0])
        t = int(input_d[1])
    
        cells = [int(x) - 1 for x in input_d[2:2+t]]

        solve(n, t, cells)