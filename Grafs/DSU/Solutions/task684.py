from typing import List
import sys

sys.setrecursionlimit(2000000)

class DSU:
    def __init__(self, n: int):
        self.parents = list(range(n))
        self.rank = [1] * n
        
    def find(self, v: int):
        if self.parents[v] == v:
            return v

        self.parents[v] = self.find(self.parents[v])
        return self.parents[v]
    
    def union(self, u: int, v: int):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u == root_v:
            return False
        
        if self.rank[root_u] < self.rank[root_v]:
            root_u, root_v = root_v, root_u
        
        self.parents[root_v] = root_u
        if self.rank[root_u] == self.rank[root_v]:
            self.rank[root_u] += 1
            
        return True 

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges)+1)
        
        for u, v in edges:
            if not dsu.union(u, v):
                return [u, v]