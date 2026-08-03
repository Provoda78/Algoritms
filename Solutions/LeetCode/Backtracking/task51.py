import sys
from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if not n: 
            return []
        
        board = [['.']*n for _ in range(n)]
        
        cols = set()
        posDiag = set()
        negDiag = set()
        
        res = []
                
        def backtracking(r: int):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                
            for c in range(n):
                if (c in cols or
                    r+c in posDiag or 
                    r-c in negDiag):
                    continue
                
                cols.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = 'Q'
                backtracking(r+1)
                
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = '.'
                
        backtracking(0)
        return res
    
if __name__ == '__main__':
    solve = Solution()
    ans = solve.solveNQueens(int(input()))
    print(ans)