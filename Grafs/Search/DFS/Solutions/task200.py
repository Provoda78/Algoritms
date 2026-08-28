class Solution:
    def numIslands(self, grid) -> int:
        if not grid:
            return 0
    
        rows = len(grid)
        colms = len(grid[0])
    
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        count_Island = 0
    
        for r in range(rows):
            for c in range(colms):
                if grid[r][c]  == '1':
                    count_Island += 1
                    grid[r][c] = '0'
            
                    stack = [(r, c)]
                    while stack:
                        cur_r, cur_c = stack.pop()
                    
                        for dr, dc in directions:
                        
                            n_r = cur_r + dr
                            n_c = cur_c + dc
                            if 0 <= n_r < rows and 0 <= n_c < colms:
                                if grid[n_r][n_c] == '1':
                                    stack.append((n_r, n_c))
                                    grid[n_r][n_c] = '0'
    
        return count_Island