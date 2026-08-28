from typing import List

def solve(arr: List[int], k: int) -> int: 
    
    left = 0
    count_nums = {}
    different = 0
    ans = 0
    
    for right in range(len(arr)):
        num = arr[right]
        
        if count_nums.get(num, 0) == 0:
            different += 1
        
        count_nums[num] = count_nums.get(num, 0) + 1
        
        while different > k:
            prev = arr[left]
            
            count_nums[prev] -= 1
            if count_nums[prev] == 0:
                different -= 1
                            
            left += 1
        
        ans = max(ans, right - left + 1)
    
    return ans