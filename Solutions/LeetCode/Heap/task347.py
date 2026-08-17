from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        nums_freq = Counter(nums)
        
        heap = []
        
        for el in nums_freq:
            par = (nums_freq[el], el)
            
            heapq.heappush(heap, par)
            if len(heap) > k:
                heapq.heappop(heap)
                
        for _, num in heap:
            res.append(num)
        
        return res
            