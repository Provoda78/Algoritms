from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtracking(start: int, path: List[int]):
            res.append(path[:])
            
            for i in range(start, len(nums)):
                
                path.append(nums[i])
                backtracking(i+1, path)
                path.pop()
        
        backtracking(0, [])
        return res