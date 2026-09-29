import sys

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    
    f = [0] * (n + 1)
    indeg = [0] * (n + 1)
    
    for i in range(1, n + 1):
        p = int(data[i])
        f[i] = p
        indeg[p] += 1
        
    dp0 = [0] * (n + 1)
    dp1 = [1] * (n + 1)
    q = [i for i in range(1, n + 1) if indeg[i] == 0]
    
    for v in q:
        p = f[v]
        a, b = dp0[v], dp1[v]
        if a > b:
            dp0[p] += a 
        else:
            dp0[p] += b
            
        dp1[p] += a
        
        indeg[p] -= 1
        if indeg[p] == 0:
            q.append(p)

    N = -10**9
    ver = [False] * (n + 1)
    ans = 0
    for s in range(1, n + 1):
        if indeg[s] == 0 or ver[s]:
            continue
        cyc = []
        v = s
        while not ver[v]:
            ver[v] = True
            cyc.append(v)
            v = f[v]
            
        c0 = cyc[0]
        best = 0
        for p0, p1, mafia in ((dp0[c0], N, False), (N, dp1[c0], True)):
            for c in cyc[1:]:
                p0, p1 = max(p0, p1) + dp0[c], p0 + dp1[c]
                
            best = max(best, p0 if mafia else max(p0, p1))
            
        ans += best
        
    print(ans)

if __name__ == '__main__':
    solve()