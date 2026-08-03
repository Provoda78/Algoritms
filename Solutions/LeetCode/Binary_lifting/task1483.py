from typing import List

class TreeAncestor:

    LOG = 16

    def __init__(self, n: int, parent: List[int]):
        self.size = n
        self.parent = parent
        self.up = [[-1]*self.LOG for _ in range(self.size)]
        
        for v in range(self.size):
            self.up[v][0] = self.parent[v]
        
        for j in range(1, self.LOG):
            for v in range(self.size):
                ancestor = self.up[v][j - 1]
                
                if ancestor != -1:
                    self.up[v][j] = self.up[ancestor][j-1]
                    
                else:
                    self.up[v][j] = -1

    def getKthAncestor(self, node: int, k: int) -> int:
        
        for j in range(self.LOG):
            if (k>>j) & 1:
                node = self.up[node][j]
                if node == -1:
                    return -1
                
        return node
                
                