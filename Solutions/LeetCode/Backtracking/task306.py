from typing import List

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        
        def backtracking(idx: int, path: List) -> bool:
            if idx == n:
                return len(path) >= 3
            
            cur_sum = 0
            for i in range(idx, n):
                
                if i > idx and num[idx] == '0':
                    break
                
                cur_sum = cur_sum*10 + int(num[i])
                
                if len(path) >= 2:
                    expected_sum = path[-1] + path[-2]
                    
                    if expected_sum > cur_sum:
                        continue
                    elif expected_sum < cur_sum:
                        break
               
                path.append(cur_sum)        
                if backtracking(i+1, path):
                    return True
            
                path.pop()
            return False

        return backtracking(0, [])