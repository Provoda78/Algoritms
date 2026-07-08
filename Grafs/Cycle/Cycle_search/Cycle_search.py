from collections import defaultdict

def has_cycle(graph: dict[list], num_vertices: int) -> bool:
    colors = {i: 0 for i in range(num_vertices)}
    
    def dfs(vertex: int) -> bool:
        colors[vertex] = 1
        
        for neighbor in graph[vertex]:
            if colors[neighbor] == 1:
                return True
            if colors[neighbor] == 0:
                if dfs(neighbor):
                    return True
        colors[vertex] = 2
        
        return False
    
    for v in range(num_vertices):
        if colors[v] == 0:
            if dfs(v):
                return True
    
    return False

#тест
if __name__ == "__main__":
    num_vertices_1 = 3
    graph_no_cycle = {0: [1], 1: [2], 2: []}
    
    num_vertices_2 = 3
    graph_with_cycle = {0: [1], 1: [2], 2: [0]}

    print("Тест 1 (Ожидается False):", has_cycle(graph_no_cycle, num_vertices_1))
    print("Тест 2 (Ожидается True):", has_cycle(graph_with_cycle, num_vertices_2))