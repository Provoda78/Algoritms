from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, curr, high = 0, 0, len(nums) - 1
        
        while curr <= high:
            if nums[curr] == 0:
                nums[curr], nums[low] = nums[low], nums[curr]
                curr += 1
                low += 1
                
            elif nums[curr] == 1:
                curr += 1
                
            elif nums[curr] == 2:
                nums[curr], nums[high] = nums[high], nums[curr]
                high -= 1