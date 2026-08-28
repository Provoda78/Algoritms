from typing import List


class Solution:

  def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
      
      n = len(temperatures)
      stack = [0]
      res = [0] * n
      
      for i in range(1, n):
            curr = temperatures[i]
          
            while stack and temperatures[stack[-1]] < curr:
              idx = stack.pop()
              dif = i - idx
              res[idx] = dif
            
            stack.append(i)
            
      return res
              