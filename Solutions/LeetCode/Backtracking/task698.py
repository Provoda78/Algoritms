from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        
        goal_sum = total_sum // k
        
        nums.sort(reverse=True)
        if nums[0] > goal_sum:
            return False
        
        subsets = [0] * k
        def backtracking(idx: int) -> bool:
            if idx == len(nums):
                return True
            
            for i in range(k):
                
                if subsets[i] + nums[idx] <= goal_sum:
                    subsets[i] += nums[idx]
                    
                    if backtracking(idx+1):
                        return True
                    
                    subsets[i] -= nums[idx]
                  
                if subsets[i] == 0:
                    break
                  
            return False
        return backtracking(0)