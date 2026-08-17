from typing import List

class Solution:

  def combine(self, n: int, k: int) -> List[List[int]]:
    res = []

    def backtrack(start: int, path: List[int]):
        
        if len(path) == k:
            res.append(path.copy())
            return

        need = k - len(path)
        bound = n - need + 1
        
        for i in range(start, bound+1):
            
            path.append(i)
            backtrack(i+1, path)
            path.pop()

    backtrack(1, [])
    return res