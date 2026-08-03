from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        colors = [0] * n        
        
        def _dfs(vertex: int):
            colors[vertex] = 1
            
            for neighbor in graph[vertex]:
                if colors[neighbor] == 1:
                    return False
                
                if colors[neighbor] == 0:
                    if not _dfs(neighbor):
                        return False
                    
            colors[vertex] = 2
            return True
        
        
        for v in range(n):
                if colors[v] == 0:
                    _dfs(v)
                    
        return [v for v in range(n) if colors[v] == 2]