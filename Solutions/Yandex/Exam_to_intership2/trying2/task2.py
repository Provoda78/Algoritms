from collections import defaultdict, deque

def zero_one_bfs(start: int, finish: int, graph) -> int:
    
    distances = defaultdict(lambda: float('inf'))    
    distances[(start, '')] = 0
    
    deq = deque([(start, '')])
    
    while deq:
        vertex, cur_color = deq.popleft()
        
        cur_dist = distances[(vertex, cur_color)]
        
        for neighbor, color in graph[vertex]:
                
            if cur_color == '' or cur_color == color:
                w = 0
            else:
                w = 1
                
            new_dist = cur_dist + w
            
            state = (neighbor, color)
            if new_dist < distances[state]:
                distances[state] = new_dist
                
                if w == 0:
                    deq.appendleft(state)
                else:
                    deq.append(state)
                    
    ans = float('inf')
    for (vertex, color), value in distances.items():
        if vertex == finish:
            ans = min(ans, value)

    return ans
                   
if __name__ == '__main__':
    
    N, M = int(input()), int(input())
    
    graph = defaultdict(list)
    
    for _ in range(M):
        u, v, color = input().split()
        
        graph[u].append((v, color))
        graph[v].append((u, color))
    
    Q = int(input())
    
    for _ in range(Q):
        start, finish = input().split()
        print(zero_one_bfs(start, finish, graph))