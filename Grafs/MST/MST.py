from typing import List, Optional

class DSU:
    def __init__(self, n: int) -> Optional['DSU']:
        self.parents = list(range(n))
        self.rank = [1] * n
        
    def find(self, v: int) -> int:
        if self.parents[v] == v:
            return v
        
        self.parents[v] = self.find(self.parents[v])
        return self.parents[v]
    
    def union(self, u: int, v: int) -> bool:
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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        edges = []
        
        for i in range(n):
            for j in range(i+1, n):
                p1, p2 = points[i], points[j]
                
                dist = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                edges.append((dist, i, j))
                
        edges.sort()
        dsu = DSU(n)
        
        mst_cost = 0
        edges_count = 0
        for d, i, j in edges:
            if dsu.union(i, j):
                mst_cost += d
                edges_count += 1
                
                if edges_count == n - 1:
                    break
        
        return mst_cost