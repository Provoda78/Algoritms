def numIslands(grid) -> int:
    if not grid:
        return 0
        
    rows = len(grid)
    cols = len(grid[0])
    islands_count = 0
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                islands_count += 1
                
                grid[r][c] = '0'
                stack = [(r, c)]
                while stack:
                    curr_r, curr_c = stack.pop()
                    
                    for dr, dc in directions:
                        neighbor_r = curr_r + dr
                        neighbor_c = curr_c + dc
                        
                        if grid[neighbor_r][neighbor_c] == '1':
                            grid[neighbor_r][neighbor_c] = '0'
                            stack.append((neighbor_r, neighbor_c))
                        
                    
    return islands_count