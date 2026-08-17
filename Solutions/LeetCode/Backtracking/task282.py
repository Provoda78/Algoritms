from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        
        res = []
        n = len(num)
        
        def backtracking(idx: int, path: str, cur_val: int, prev_val: int):
            if idx == n:
                if cur_val == target:
                    res.append(path)
                return
            
            for i in range(idx, n):
                if i > idx and num[idx] == "0":
                    break
                
                curr_str = num[idx:i+1]
                cur_num = int(curr_str)
                
                if idx == 0:
                    backtracking(i+1, path+curr_str, cur_num, cur_num)
                else:
                    backtracking(i+1, path+'+'+curr_str, cur_val+cur_num, cur_num)
                    backtracking(i+1, path+'-'+curr_str, cur_val-cur_num, -cur_num)
                    backtracking(i+1, path+'*'+curr_str, cur_val - prev_val + (prev_val * cur_num), 
                                 prev_val*cur_num)
                    
        backtracking(0, '', 0, 0)
        return res