from collections import defaultdict

def dfs(graph, vertex, visited=None):
    if visited is None:
        visited = set()
        
    visited.add(vertex)
    print(vertex, end=" ")
    
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
            
def dfs_iterative(graph, start_vertex):
    visited = set()
    stack = [(start_vertex)]
    
    while stack:
        vertex = stack.pop()
        
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=" ")
            
            for neighbor in graph[vertex]:
                stack.append(neighbor)

test_graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 4],
    4: [2, 3]
}

dfs_iterative(test_graph, 1)
        