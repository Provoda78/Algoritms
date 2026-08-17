from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    
    if not intervals:
        return []
    
    intervals.sort()
  
    res = [intervals[0]]
  
    for i in range(1, len(intervals)):
        interval = intervals[i]
        prev = res[-1]
      
        if prev[1] >= interval[0]:
            res[-1][1] = max(prev[1], interval[1])        
        else:
            res.append(interval)

    return res
  