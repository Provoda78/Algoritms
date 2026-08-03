from typing import Optional, List

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
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """           
        
        ROWS, COLMS = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        dsu = DSU(ROWS*COLMS+1)
        dummy_border = ROWS * COLMS
        
        for r in range(ROWS):
            for c in range(COLMS):
                if board[r][c] == 'O':
                    idx_cell = COLMS * r + c
                
                    for dr, dc in directions:
                    
                        r_neighbor = r + dr
                        c_neighbor = c + dc
                     
                        if (0 <= r_neighbor < ROWS and 
                                0 <= c_neighbor < COLMS):               
                            if board[r_neighbor][c_neighbor] == 'O': 
                        
                                idx_neighbor = COLMS * r_neighbor + c_neighbor
                                dsu.union(idx_cell, idx_neighbor)
                        
                        else:
                            dsu.union(idx_cell, dummy_border)
                        
        for r in range(ROWS):
            for c in range(COLMS):
                if board[r][c] == 'O':
                    idx_cell = COLMS * r + c
                    if dsu.find(idx_cell) != dsu.find(dummy_border):
                        board[r][c] = 'X'