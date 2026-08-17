from typing import List
from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        @cache       
        def backtracking(path, idx):
            
            if idx == len(nums):
                return 1 if path == target else 0
                
            sum_ = backtracking(path+nums[idx], idx+1)
            subsum = backtracking(path-nums[idx], idx+1)
            
            return sum_ + subsum
            
        return backtracking(0, 0)
                
                
                