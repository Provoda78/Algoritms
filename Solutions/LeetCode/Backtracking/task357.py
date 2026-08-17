from typing import List

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        
        if n == 0:
            return 1
        
        ans = 10
        cur_count = 9
        choices = 9
        
        for _ in range(2, n+1):
            cur_count *= choices
            ans += cur_count
            choices -= 1
        
        return ans
            