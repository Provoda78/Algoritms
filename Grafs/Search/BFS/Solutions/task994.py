from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        
        freshs = 0
        
        deg = deque([])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    freshs += 1
                    
                if grid[r][c] == 2:
                    deg.append((r, c))
                    
        if freshs == 0:
            return 0
                                
        while deg and freshs > 0:
            
            minutes += 1
            
            for _ in range(len(deg)):
                
                r, c = deg.popleft()
                
                for dr, dc in directions:
                    r_neighbor = r + dr
                    c_neighbor = c + dc
                    
                    if (0 <= r_neighbor < len(grid) and 
                        0 <= c_neighbor < len(grid[0]) and 
                        grid[r_neighbor][c_neighbor] == 1):
                    
                        grid[r_neighbor][c_neighbor] = 2
                        freshs -= 1
                        deg.append((r_neighbor, c_neighbor))
            
        return minutes if freshs == 0 else -1