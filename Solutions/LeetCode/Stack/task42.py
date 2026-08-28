from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
            
        stack = []
        water = 0
            
        for i in range(len(height)):
            curr = height[i]
                
            while stack and curr > height[stack[-1]]:
                bottom = stack.pop()
                    
                if not stack:
                    break
                
                left = stack[-1]
                    
                h = min(curr, height[left]) - height[bottom]
                w = i - left - 1
                    
                water += h*w
            
            stack.append(i)
                
        return water