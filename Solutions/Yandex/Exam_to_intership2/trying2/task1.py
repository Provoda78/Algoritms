from typing import List
from collections import deque

def solve(nums: List[int], k: int) -> int:
    res = 0
    deq_max = deque()
    deq_min = deque()
    
    left = 0
    for i, num in enumerate(nums):
        
        while deq_max and num >= nums[deq_max[-1]]:
            deq_max.pop()
        
        while deq_min and num <= nums[deq_min[-1]]:
            deq_min.pop()
            
        deq_max.append(i)
        deq_min.append(i)
        
        while nums[deq_max[0]] - nums[deq_min[0]] > k:
                        
            if deq_min[0] == left:
                deq_min.popleft()
            
            if deq_max[0] == left:
                deq_max.popleft()
            
            left += 1
        
        res = max(res, i - left + 1)

    return res