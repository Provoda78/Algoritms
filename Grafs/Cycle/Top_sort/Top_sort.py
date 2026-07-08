from collections import defaultdict

def top_sort(graph: dict[list], num_vertices: int) -> bool:
    colors = {i: 0 for i in range(num_vertices)}
    order = []
    
    def dfs(vertex: int) -> bool:
        colors[vertex] = 1
        
        for neighbor in graph[vertex]:
            if colors[neighbor] == 1:
                return True
            if colors[neighbor] == 0:
                if dfs(neighbor):
                    return True
                
        colors[vertex] = 2
        order.append(vertex)
        
        return False
    
    for v in range(num_vertices):
        if colors[v] == 0:
            if dfs(v):
                return []
    
    return order[::-1]

if __name__ == "__main__":
    #Тест 1: Успешная сортировка (DAG)
    num_vertices_1 = 5
    graph_dag = {
        0: [2],
        1: [3],
        3: [4, 2],
        2: [],
        4: []
    }

    #Тест 2: Есть цикл (сортировка невозможна)
    num_vertices_2 = 3
    graph_cycle = {0: [1], 1: [2], 2: [0]}
    
    result_1 = top_sort(graph_dag, num_vertices_1)
    result_2 = top_sort(graph_cycle, num_vertices_2)
    
    print("Тест 1 (Правильный порядок):", result_1) 
    # Возможный корректный вывод: [1, 3, 4, 0, 2] или [0, 1, 3, 2, 4] 
    # Главное, чтобы 1 было раньше 3, 3 раньше 4 и 2, а 0 раньше 2.
    
    print("Тест 2 (Ожидается []):", result_2)