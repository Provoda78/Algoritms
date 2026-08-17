from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def can_eat(speed: int) -> bool:
            hours = sum([(p + speed - 1) // speed for p in piles])
            return hours <= h
        
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left+right) // 2
            
            if can_eat(mid):
                right = mid
            else:
                left = mid + 1
        
        return left