from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0
        
        while left < right:
            
            cur_left = height[left]
            cur_right = height[right]
            
            if cur_left > left_max:
                left_max = cur_left
            if cur_right > right_max:
                right_max = cur_right
            
            if left_max <= right_max:
                water += left_max - height[left]
                left += 1
            else:
                water += right_max - height[right]
                right -= 1
        
        return water