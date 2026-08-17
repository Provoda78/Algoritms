from typing import List

class Solution:

  def productExceptSelf(self, nums: List[int]) -> List[int]:
      
    n = len(nums)
    pref_left = [1] * (n + 1)
    pref_right = [1] * (n + 1)

    for i in range(1, n + 1):
      pref_left[i] = pref_left[i - 1] * nums[i - 1]

    for i in range(n - 1, -1, -1):
      pref_right[i] = pref_right[i + 1] * nums[i]

    return [pref_left[i] * pref_right[i + 1] for i in range(n)]