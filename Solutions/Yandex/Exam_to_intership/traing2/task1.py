import sys
from typing import List


def prefix_sum(arr: List[int]) -> List[int]:
  res = [0] * (len(arr) + 1)
  for i in range(1, len(arr) + 1):
    res[i] = res[i - 1] + arr[i - 1]
  return res


def solve() -> int:
  input_data = sys.stdin.read().split()
  if not input_data:
    return 0

  nums = [int(x) for x in input_data[:-1]]
  k = int(input_data[-1])

  pref_sum = prefix_sum(nums)

  count_sum = {0: 1}
  result = 0

  for i in range(1, len(pref_sum)):
    curr_sum = pref_sum[i]

    result += count_sum.get(curr_sum - k, 0)
    count_sum[curr_sum] = count_sum.get(curr_sum, 0) + 1

  return result