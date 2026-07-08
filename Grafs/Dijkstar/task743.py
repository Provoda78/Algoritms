from typing import List
from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        
        for v1, v2, w in times:
            graph[v1].append((v2, w))
            
        distances = {i: float('inf') for i in range(1, n+1)}
        distances[k] = 0
        
        min_heap = [(0, k)]
        while min_heap:
            
            dist, vertex = heapq.heappop(min_heap)
            if dist > distances[vertex]:
                continue
            
            for neighbor, weight in graph[vertex]:
                new_dist = dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(min_heap, (new_dist, neighbor))
                    
        all_times = distances.values()
        
        for time in all_times:
            if time == float('inf'):
                return -1
            
        return max(all_times)