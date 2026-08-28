class DSU:
    def __init__(self, n: int):
        
        self.parents = list(range(n+1))
        self.size = [1] * (n+1)
        
    def find(self, v: int) -> int:
        if v == self.parents[v]:
            return v
        
        self.parents[v] = self.find(self.parents[v])
        return self.parents[v]
    
    def union(self, u: int, v: int) -> bool:
        
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u == root_v:
            return False
        
        if self.size[root_u] < self.size[root_v]:
            root_u, root_v = root_v, root_u
            
        self.parents[root_v] = root_u
        self.size[root_u] += self.size[root_v]
            
        return True
    
def destruction_of_roads():
    N, M = map(int, input().split())
    
    edges = [None] * (M+1)
    remove_edges = []
    
    for i in range(1, M+1):
        edges[i] = list(map(int, input().split()))
        
    Q = int(input())
    
    for _ in range(Q):
        idx = int(input())
        
        remove_edges.append(edges[idx])
        edges[idx] = None
        
    components = N
    dsu = DSU(N)

    for i in range(1, M+1):
        edge = edges[i]
        
        if edge:
            u, v = map(int, edge)
            if dsu.union(u, v):
                components -= 1
                
    ans = []
    for i in range(len(remove_edges)-1, -1, -1):
        u, v = remove_edges[i]
        
        ans.append(components == 1)
        
        if dsu.union(u, v):
            components -= 1
    
    return ans
            
if __name__ == '__main__':
    res = destruction_of_roads()
    
    for i in range(len(res)-1, -1, -1):
        print(res[i])