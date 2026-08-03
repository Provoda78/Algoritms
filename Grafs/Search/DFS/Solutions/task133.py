class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        stack = [node]
                
        old_to_new = {node: Node(node.val)}
        
        while stack:
            v = stack.pop()
                
            for neighbor in v.neighbors:
                if neighbor not in old_to_new:
                    stack.append(neighbor)
            
                    old_to_new[neighbor] = Node(neighbor.val)
                    
                old_to_new[v].neighbors.append(old_to_new[neighbor])
        
        return old_to_new[node]