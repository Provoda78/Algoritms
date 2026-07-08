from collections import deque

def bfs(graph, start_vertex=1):
    visited = {start_vertex}
    deq = deque([start_vertex])
    
    while deq:
        vertex = deq.popleft()
        print(vertex, end=" ")
            
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                deq.append(neighbor)
    
test_graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 4],
    4: [2, 3]
}

bfs(test_graph)