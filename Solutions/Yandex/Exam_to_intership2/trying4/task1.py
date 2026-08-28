from typing import List
from collections import defaultdict

class LCA:

    LOG = 19
    
    def __init__(self, n: int, parent: List[int], value: List[int]):
        
        self.size = n
        self.value = value
        self.up = [[[-1, 0] for _ in range(self.LOG)] for _ in range(n+1)]
        self.depth = [0] * (self.size+1)
        
        
        graph = defaultdict(list)
        root = 1
        for v in range(1, n+1):
            if parent[v] == -1:
                root = v
            else:
                graph[parent[v]].append(v)
        
        self._dfs(root, -1, 0, graph)
        
        for v in range(1, self.size+1):
            if parent[v] != -1:
                self.up[v][0][1] = value[parent[v]]
            
        for v in range(1, self.size+1):
            for j in range(1, self.LOG):
                ancestor = self.up[v][j-1][0]
                
                if ancestor != -1:
                    self.up[v][j][0] = self.up[ancestor][j-1][0]
                    self.up[v][j][1] = self.up[v][j-1][1] + self.up[ancestor][j-1][1]
                    
    def _dfs(self, v: int, p: int, d: int, graph: dict):
            self.depth[v] = d
            self.up[v][0][0] = p
                        
            for neighbor in graph[v]:
                if neighbor != p:
                    self._dfs(neighbor, v, d + 1, graph)
                    
    def get_LCA(self, u: int, v: int) -> int:
        if self.depth[u] < self.depth[v]:
            u, v = v, u
            
        diff = self.depth[u] - self.depth[v]
        
        for j in range(1, self.LOG):
            if diff & (1 << j):
                u = self.up[u][j][0]
          
        if u == v:
            return u
                
        for j in range(self.LOG - 1, -1, -1):
            if self.up[u][j][0] != self.up[v][j][0]:
                u = self.up[u][j][0]
                v = self.up[v][j][0]
            
        return self.up[u][0][0]
    
    def query(self, u: int, v: int) -> int:
        l = self.get_LCA(u, v)

        def climb_sum(x: int, steps: int) -> int:
            res = 0
            bit = 0
            while steps:
                if steps & 1:
                    res += self.up[x][bit][1]
                    x = self.up[x][bit][0]
                steps >>= 1
                bit += 1
            return res

        # u -> lca, включая u и l
        sum_u = self.value[u] + climb_sum(u, self.depth[u] - self.depth[l])

        # v -> lca, включая v и l
        sum_v = self.value[v] + climb_sum(v, self.depth[v] - self.depth[l])

        # lca посчитан дважды
        return sum_u + sum_v - self.value[l]