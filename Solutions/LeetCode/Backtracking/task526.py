from typing import Set

class Solution:
    def countArrangement(self, n: int) -> int:
        count_ = 0
        
        path = [0] * n
        def backtracking(idx: int, visited: Set):
            nonlocal count_
            
            if idx == n+1:
                count_ += 1
                return
            
            #выбираем число
            for i in range(1, n+1):
                if (i not in visited) and (idx % i == 0 or i % idx == 0):
                    visited.add(i)
                    backtracking(idx+1, visited)
                    visited.remove(i)
                            
        backtracking(1, set())   
        return count_