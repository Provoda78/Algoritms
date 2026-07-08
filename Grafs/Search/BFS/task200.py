from collections import deque
class Solution:
    def shortestPath(grid) -> int:
        if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        n = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
        dec = deque([(0, 0, 1)])
        grid[0][0] = 1
        
        while dec:
            r, c, cur_dist = dec.popleft()
            
            if r == n-1 and c == n-1:
                return cur_dist
            
            for dr, dc in directions:
                neighbor_r = r + dr
                neighbor_c = c + dc
                if 0 <= neighbor_r < n and 0 <= neighbor_c < n:
                    if grid[neighbor_r][neighbor_c] == 0:
                        grid[neighbor_r][neighbor_c] = 1
                        dec.append((neighbor_r, neighbor_c, cur_dist+1))
                    
        return -1
    