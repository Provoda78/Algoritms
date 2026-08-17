from typing import List

class Solution:
        def numsSameConsecDiff(self, n: int, k: int) -> List[int]:

            path = []
            def backtracking(idx, num):
                nonlocal path
                
                if idx == n:
                    path.append(num)
                    return
                    
                last = num%10
                
                need_nums = {last-k, last+k}
                for dig in need_nums:
                    if 0<=dig<=9:
                        backtracking(idx+1,  num*10 + dig)
              
            for i in range(1, 10):  
                backtracking(1, i)
            return path
                    