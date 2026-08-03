from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        rows = [0]*9
        colms = [0]*9
        boxs = [0]*9
        
        empty_cells = []
        
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    num = 1 << int(board[r][c])
                    box_idx = (r//3) * 3 + (c//3)
                    
                    rows[r] |= num
                    colms[c] |= num
                    boxs[box_idx] |= num
                
                else:
                    empty_cells.append((r, c))
        
        def backtracking(idx: int ) -> bool:
            if idx == len(empty_cells):
                return True
            
            r, c = empty_cells[idx]
            box_idx = (r//3) * 3 + (c//3)
            
            used = rows[r] | colms[c] | boxs[box_idx]
                
            for num in range(1, 10):
                mask = 1 << num
                    
                if not (mask & used):
                    rows[r] |= mask
                    colms[c] |= mask
                    boxs[box_idx] |= mask
                    board[r][c] = str(num)
                        
                    if backtracking(idx+1):
                        return True
                        
                    rows[r] ^= mask
                    colms[c] ^= mask
                    boxs[box_idx] ^= mask
                    board[r][c] = '.'
                    
            return False
                        
        backtracking(0)
        
if __name__ == '__main__':
  solve = Solution()

  board = [
      ["5", "3", ".", ".", "7", ".", ".", ".", "."],
      ["6", ".", ".", "1", "9", "5", ".", ".", "."],
      [".", "9", "8", ".", ".", ".", ".", "6", "."],
      ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
      ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
      ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
      [".", "6", ".", ".", ".", ".", "2", "8", "."],
      [".", ".", ".", "4", "1", "9", ".", ".", "5"],
      [".", ".", ".", ".", "8", ".", ".", "7", "9"],
  ]

  solve.solveSudoku(board)

  for row in board:
    print(row)
                    