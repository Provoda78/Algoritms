from collections import defaultdict
from typing import List

class Solution:
    
  def subarraySum(self, nums: List[int], k: int) -> int:
    count_sum = defaultdict(int)
    count_sum[0] = 1

    curr_sum = 0
    result = 0

    for num in nums:
      curr_sum += num

      result += count_sum[curr_sum - k]

      count_sum[curr_sum] += 1

    return result