from collections import defaultdict
from typing import List

class TreeAncestor:

    LOG = 16

    def __init__(self, n: int, parent: List[int]):
        self.size = n
        self.up = [[-1] * self.LOG for _ in range(self.size)]
        self.depth = [0] * self.size

        graph = defaultdict(list)
        root = 0
        for v in range(n):
            if parent[v] == -1:
                root = v
            else:
                graph[parent[v]].append(v)

        self._dfs(root, -1, 0, graph)

        for j in range(1, self.LOG):
            for v in range(self.size):
                ancestor = self.up[v][j - 1]
                if ancestor != -1:
                    self.up[v][j] = self.up[ancestor][j - 1]

    def _dfs(self, v: int, p: int, d: int, graph: dict):
        self.depth[v] = d
        self.up[v][0] = p
        
        for neighbor in graph[v]:
            if neighbor != p:
                self._dfs(neighbor, v, d + 1, graph)

    def get_lca(self, u: int, v: int) -> int:
        if self.depth[u] < self.depth[v]:
            u, v = v, u
            
        diff = self.depth[u] - self.depth[v]
        
        for j in range(self.LOG):
            if (diff >> j) & 1:
                u = self.up[u][j]
                
        if u == v:
            return u
        
        for j in range(self.LOG - 1, -1, -1):
            if self.up[u][j] != self.up[v][j]:
                u = self.up[u][j]
                v = self.up[v][j]
                
        return self.up[u][0]