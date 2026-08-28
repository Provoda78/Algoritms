from collections import deque

def zero_one_bfs(graph, start, num_vertices):
    # Инициализируем расстояния бесконечностью
    distances = [float('inf')] * num_vertices
    distances[start] = 0
    
    # Создаем дек и добавляем стартовую вершину
    queue = deque([start])
    
    while queue:
        u = queue.popleft()
        
        # Обходим всех соседей вершины u
        for v, weight in graph[u]:
            # Условие релаксации ребра
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                
                # Если вес 0 — добавляем в начало, если 1 — в конец
                if weight == 0:
                    queue.appendleft(v)
                else:
                    queue.append(v)
                    
    return distances

# --- Пример использования ---
# Граф из 5 вершин (0, 1, 2, 3, 4)
# Представление: graph[u] = [(v1, weight1), (v2, weight2), ...]
num_v = 5
graph = {i: [] for i in range(num_v)}

# Добавляем ребра (откуда, куда, вес)
edges = [
    (0, 1, 1),
    (0, 2, 0),
    (1, 3, 1),
    (2, 1, 0),
    (2, 4, 1),
    (3, 4, 0)
]

for u, v, w in edges:
    graph[u].append((v, w))
    # Если граф неориентированный, раскомментируйте строку ниже:
    # graph[v].append((u, w))

start_vertex = 0
result = zero_one_bfs(graph, start_vertex, num_v)

# Вывод результатов
print(f"Кратчайшие расстояния от вершины {start_vertex}:")
for vertex, dist in enumerate(result):
    print(f"До вершины {vertex}: {dist}")