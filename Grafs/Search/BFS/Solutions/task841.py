from typing import List
from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        deq = deque([0])
        visited = {0}
        
        while deq:
            vertex = deq.popleft()
                
            for i in rooms[vertex]:
                if i not in visited:
                    deq.append(i)
                    visited.add(i)

        
        return len(visited) == len(rooms)