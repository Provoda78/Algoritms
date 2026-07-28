import sys

class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
class BST:
    def insert(self, value: int, root: Node):
        if not (root):
            return Node(value)
        
        if value < root.value:
            root.left = self.insert(value, root.left)
        
        elif value > root.value:
            root.right = self.insert(value, root.right)
            
        return root
    
    def height(self, root: Node):
        if root is None:
            return 0
            
        left_height = self.height(root.left)
        right_height = self.height(root.right)
    
        return max(left_height, right_height) + 1
    
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    bst = BST()
    root = None
    
    for item in input_data:
        val = int(item)
        if val == 0:
            break
        root = bst.insert(val, root)
        
    print(bst.height(root))

if __name__ == "__main__":
    solve()
    