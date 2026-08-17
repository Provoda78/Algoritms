import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return []

    nums = [int(x) for x in input_data]

    nums.append(nums[0])
    res = []
    
    n = len(nums)
    first, end = 0, 0
    
    while end < n-1:
        
        if end + 1 < n and nums[end+1] == nums[end] + 1:
            end += 1
        
        elif end + 1 < n and nums[end+1] != nums[end] + 1:
            res.append(f'{nums[first]}->{nums[end]}' if first != end else str(nums[first]))
            end += 1
            first = end
    
    return res