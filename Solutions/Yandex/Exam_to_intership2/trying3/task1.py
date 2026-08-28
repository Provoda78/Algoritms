from typing import List, Dict
from collections import defaultdict
import sys

sys.setrecursionlimit(300000)

def the_longest_path(start: int, graph: Dict[int, List[int]]) -> int:
    ans = 0
    
    visited = set()
    def dfs(vertex: int, depth: int) -> None:
        nonlocal ans
        
        ans = max(ans, depth)
        visited.add(vertex)
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs(neighbor, depth+1)
    
    dfs(start, 0)
    return ans

if __name__ == '__main__':
    N, M = map(int, input().split())
    
    graph = defaultdict(list)
    
    for _ in range(M):
        u, v = map(int, input().split())
        
        graph[u].append(v)
        graph[v].append(u)
    
    print(the_longest_path(1, graph))