from typing import List
from math import sqrt
import heapq

class Ordered_set:
    def __init__(self):
        pass
    
    def next(self, val):
        pass
    
    def prev(self, val):
        pass
    
    def insert(self):
        pass
    
    def erase(self):
        pass

class Mo:
    def __init__(self):
        
        self.current_min = float('inf')
        self.s = Ordered_set()
        self.gap_count = {}
        self.heap = []
        
    def add(self, val: int):
        left = self.s.prev(val)
        right = self.s.next(val)

        if left is not None and right is not None:
            self._remove_gap(right - left)

        if left is not None:
            self._add_gap(val - left)

        if right is not None:
            self._add_gap(right - val)

        self.s.insert(val)

        while self.heap and self.gap_count.get(self.heap[0], 0) == 0:
            heapq.heappop(self.heap)

        self.current_min = self.heap[0] if self.heap else float('inf')
    
    def remove(self, val: int):
        left = self.s.prev(val)
        right = self.s.next(val)

        if left is not None:
            self._remove_gap(val - left)

        if right is not None:
            self._remove_gap(right - val)

        if left is not None and right is not None:
            self._add_gap(right - left)
            
        self.s.erase(val)

        while self.heap and self.gap_count.get(self.heap[0], 0) == 0:
            heapq.heappop(self.heap)

        self.current_min = self.heap[0] if self.heap else float('inf')
                
    def _add_gap(self, gap):
        self.gap_count[gap] = self.gap_count.get(gap, 0) + 1
        heapq.heappush(self.heap, gap)
    
    def _remove_gap(self, gap):
        self.gap_count[gap] -= 1

        if self.gap_count[gap] == 0:
            del self.gap_count[gap]
            
def solve() -> List[int]:
    N, Q = list(map(int, input().split()))
    
    B = int(sqrt(N))
    
    res = [0] * Q
    queries = []
    arr = [0] + list(map(int, input().split()))
    if len(arr) < 2:
        return [0]
    
    for idx in range(Q):
        l, r = map(int, input().split())
        queries.append((l, r, idx))
        
    queries.sort(key= lambda q: (q[0] // B, q[1]))
    mo = Mo()
    
    cur_l = 1
    cur_r = 0
    for l, r, idx in queries:
        
        while cur_l > l:
            cur_l -= 1
            mo.add(arr[cur_l])

        while cur_r < r:
            cur_r += 1
            mo.add(arr[cur_r])

        while cur_l < l:
            mo.remove(arr[cur_l])
            cur_l += 1

        while cur_r > r:
            mo.remove(arr[cur_r])
            cur_r -= 1
        
        res[idx] = mo.current_min
    
    return res
        
if __name__ == '__main__':
    answers = solve()
    
    for ans in answers:
        print(ans, sep='\n')