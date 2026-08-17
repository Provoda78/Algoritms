from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        
        prefixs = {0: -1}
        curr_prefix = 0
        max_len, curr_len = 0, 0
        
        for i in range(len(nums)):
            
            if nums[i] == 0:
                curr_prefix -= 1
            else:
                curr_prefix += 1
            
            if curr_prefix in prefixs:
                curr_len = i - prefixs[curr_prefix]
                
                if curr_len > max_len:
                    max_len = curr_len
                    
            else:
                prefixs[curr_prefix] = i

        return max_len