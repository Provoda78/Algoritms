from typing import List

class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
  
        n = len(temperatures)
  
        res = [0] * n
        stack = []
        
        for i in range(n):
            
            curr_temp = temperatures[i]
            while stack and curr_temp >= temperatures[stack[-1]]:
                
                prev_i = stack.pop()
                res[prev_i] = i - prev_i
            
            stack.append(i)
        
        return res