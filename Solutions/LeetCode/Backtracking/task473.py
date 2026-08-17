from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        g_sum = sum(matchsticks)
        
        if g_sum % 4 != 0 or len(matchsticks) < 4:
            return False
        
        need_side = g_sum // 4
        
        matchsticks.sort(reverse=True)
        if need_side < matchsticks[0]:
            return False
        
        sides = [0] * 4
        def backtracking(idx: int):
            
            if idx == len(matchsticks):
                return True
            
            for i in range(4):
                
                if sides[i] + matchsticks[idx] <= need_side:
                    sides[i] += matchsticks[idx]
                
                    if backtracking(idx+1):
                        return True

                    sides[i] -= matchsticks[idx]
                
                if sides[i] == 0:
                    break
                
            return False
        return backtracking(0)
                                    