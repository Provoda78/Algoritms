import heapq
from collections import defaultdict

def dijkstra(graph, start_vertex, num_vertices, traget_vertex=None):
    distances = {i: float('inf') for i in range(1, num_vertices+1)}
    distances[start_vertex] = 0
    
    parent = {i: None for i in range(1, num_vertices+1)}
    
    min_heap = [(0, start_vertex)]
    
    while min_heap:
        dist, vertex = heapq.heappop(min_heap)
        
        if traget_vertex and traget_vertex == vertex:
            break
        
        if dist > distances[vertex]:
            continue
        
        for neighbor, weight in graph[vertex]:
            distance_new = dist + weight
            if distance_new < distances[neighbor]:
                
                distances[neighbor] = distance_new
                parent[neighbor] = vertex
                heapq.heappush(min_heap, (distance_new, neighbor))
                
    return distances, parent

def path_to_target(parent, start, target):
    path = []
    
    current = target
    while current is not None:
        path.append(current)
        current = parent[current]
        
    path.reverse()
    
    return path if path[0] == start else []

if __name__ == "__main__":
    
    #1 -> 2 с весом 5
    #1 -> 3 с весом 2
    #3 -> 2 с весом 1
    test_graph = {
        1: [(2, 5), (3, 2)],
        2: [],
        3: [(2, 1)]
    }
    
    num_vertices = 3
    start = 1
    target = 2
    
    #Запуск алгоритма
    distances, parent = dijkstra(test_graph, start, num_vertices)
    path = path_to_target(parent, start, target)
    
    print("--- Проверка Дейкстры ---")
    print(f"Кратчайшее расстояние от {start} до {target}: {distances[target]}") 
    #Ожидается: 3
    
    print(f"Оптимальный маршрут: {path}") 
    #Ожидается: [1, 3, 2]
    

    