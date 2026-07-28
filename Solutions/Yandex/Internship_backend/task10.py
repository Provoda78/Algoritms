import sys
sys.setrecursionlimit(2000000)

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        
    def find(self, v: int) -> int:
        
        if self.parent[v] == v:
            return v
        self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
    
    def union(self, a: int, b: int) -> bool:
        
        root_a = self.find(a)
        root_b = self.find(b)
        
        if root_a == root_b:
            return False
        
        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a
            
        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]
        return True
    
def solve():
    
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    heights = [int(x) for x in input_data[1:n+1]]
    
    dsu = DSU(n)
    events = [(height, idx) for idx, height in enumerate(heights)]
    events.sort(reverse=True)
    
    active = [False] * n
    max_area = 0
    
    for height, idx in events:
        active[idx] = True
        
        if idx > 0 and active[idx - 1]:
            dsu.union(idx - 1, idx)
            
        if idx + 1 < n and active[idx + 1]:
            dsu.union(idx + 1, idx)
                
        current_width = dsu.size[dsu.find(idx)]
        current_area = height * current_width
        
        if current_area > max_area:
            max_area = current_area
            
    print(max_area)

if __name__ == "__main__":
    solve()