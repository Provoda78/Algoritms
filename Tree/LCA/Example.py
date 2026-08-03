from typing import List, Dict
from collections import defaultdict

class CompanyLCA:
    
    LOG = 10
    
    def __init__(self, n:int, boss: List):
        self.size = n
        self.parent = boss
        self.up = [[-1] * self.LOG for _ in range(self.size)]
        self.depth = [0] * self.size
        
        graph = defaultdict(list)
        root = 0
        
        for v in range(self.size):
            if self.parent[v] == -1:
                root = v
                
            else:
                graph[self.parent[v]].append(v)
                
        self._dfs(root, -1, 0, graph)
                
        for j in range(1, self.LOG):
            for v in range(self.size):
                ancestor = self.up[v][j-1]
                
                if ancestor != -1:
                    self.up[v][j] = self.up[ancestor][j-1]
                    
    def _dfs(self, v:int, p:int, d:int, graph: Dict[int, List]):
        self.up[v][0] = p
        self.depth[v] = d
        
        for neighbor in graph[v]:
            if neighbor != p:
                self._dfs(neighbor, v, d+1, graph)
        
        
    def get_lca(self, u: int, v: int) -> int:
        
        if self.depth[u] < self.depth[v]:
            u, v = v, u
            
        diff = self.depth[u] - self.depth[v]   
        for j in range(self.LOG):
            if (diff >> j) & 1:
                u = self.up[u][j]
                
        if u == v:
            return v
        
        for j in range(self.LOG-1, -1, -1):
            if self.up[u][j] != self.up[v][j]:
                u = self.up[u][j]
                v = self.up[v][j]
        
        return self.up[u][0]
    
    
if __name__ == '__main__':
    # Дерево из 5 вершин: 0 — корень (CEO)
    # 1 и 2 подчиняются 0
    # 3 и 4 подчиняются 1
    # boss: node 0 -> -1, node 1 -> 0, node 2 -> 0, node 3 -> 1, node 4 -> 1
    boss = [-1, 0, 0, 1, 1]
    company = CompanyLCA(5, boss)
    
    print("LCA(3, 4) =", company.get_lca(3, 4))  # Ожидается: 1
    print("LCA(3, 2) =", company.get_lca(3, 2))  # Ожидается: 0
    print("LCA(0, 4) =", company.get_lca(0, 4))  # Ожидается: 0