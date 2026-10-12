from collections import defaultdict, deque
from typing import List

def top_sort_Kan(num_v: int, edges: List[List[int]]) -> List[int]:
    res = []
    
    graph = defaultdict(list)
    in_degree = [0] * num_v
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
        
    deq = deque([i for i in range(len(in_degree)) if in_degree[i] == 0])
    
    while deq:
        vertex = deq.popleft()
        res.append(vertex)
        
        for neighbor in graph[vertex]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                deq.append(neighbor)
                
    if len(res) != num_v:
        return []
    
    return res
    
if __name__ == "__main__":
    #Тест 1: Успешная сортировка (DAG)
    num_vertices_1 = 5
    graph_dag = [[0, 2], [1, 3], [3, 4], [3, 2]]

    #Тест 2: Есть цикл (сортировка невозможна)
    num_vertices_2 = 3
    graph_cycle = [[0, 1], [1, 2], [2, 0]]
    
    result_1 = top_sort_Kan(num_vertices_1, graph_dag)
    result_2 = top_sort_Kan(num_vertices_2, graph_cycle)
    
    print("Тест 1 (Правильный порядок):", result_1) 
    # Возможный корректный вывод: [1, 3, 4, 0, 2] или [0, 1, 3, 2, 4] 
    # Главное, чтобы 1 было раньше 3, 3 раньше 4 и 2, а 0 раньше 2.
    
    print("Тест 2 (Цикл, Ожидается []):", result_2)