from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows, colms = len(board), len(board[0])
        
        def backtracking(r: int, c: int, idx: int):
            
            if idx == len(word):
                return True
            
            if r < 0 or c < 0 or r >= rows or c >= colms or board[r][c] != word[idx]:
                return False
            
            temp = board[r][c]
            board[r][c] = '#'
            
            flag = (backtracking(r, c+1, idx+1) or
                    backtracking(r-1, c, idx+1) or 
                    backtracking(r+1, c, idx+1) or
                    backtracking(r, c-1, idx+1))
            
            board[r][c] = temp
            
            return flag
        for i in range(rows):
            for j in range(colms):
                if backtracking(i, j, 0):
                    return True
                
        return False
                
                
if __name__ == '__main__':
    solve = Solution()
    ans = solve.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED")                    
    print(ans)  