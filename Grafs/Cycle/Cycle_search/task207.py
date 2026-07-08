from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for a, b in prerequisites:
            graph[b].append(a)
            
        colors = {i: 0 for i in range(numCourses)}
        
        def dfs(vertex):
            colors[vertex] = 1
            
            for neighbor in graph.get(vertex, []):
                if colors[neighbor] == 1:
                    return True
                if colors[neighbor] == 0:
                    if dfs(neighbor):
                        return True
                    
            colors[vertex] = 2
            return False
        
        for v in range(numCourses):
            if colors[v] == 0:
                if dfs(v):
                    return False
                
        return True
                