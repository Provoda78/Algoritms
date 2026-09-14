import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    n = int(next(iterator))
    q = int(next(iterator))
    
    parent = [list(range(n + 1)) for _ in range(10)]
    components = [n] * 10
    
    def find(w, i):
        root = i
        while parent[w][root] != root:
            root = parent[w][root]
        curr = i
        while curr != root:
            nxt = parent[w][curr]
            parent[w][curr] = root
            curr = nxt
        return root

    def union(w, u, v):
        root_u = find(w, u)
        root_v = find(w, v)
        if root_u != root_v:
            parent[w][root_u] = root_v
            components[w] -= 1
            return True
        return False

    def add_edge(u, v, c):
        for w in range(c, 10):
            union(w, u, v)

    for _ in range(n - 1):
        u = int(next(iterator))
        v = int(next(iterator))
        c = int(next(iterator))
        add_edge(u, v, c)

    res = []
    for _ in range(q):
        u = int(next(iterator))
        v = int(next(iterator))
        w = int(next(iterator))
        
        add_edge(u, v, w)
        
        mst_weight = n - 10
        for w_val in range(1, 10):
            mst_weight += components[w_val]
            
        res.append(str(mst_weight))
        
    return res

if __name__ == '__main__':
    ans = solve()
    
    for w in ans:
        print(w)