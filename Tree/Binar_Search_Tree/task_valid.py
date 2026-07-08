class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
def valid(node, low, high):
    if not node:
        return True
    if node.val < low or node.val > high:
        return False
    return True

def is_binar_tree(head):
    
    prev = float('-inf')
     
    def inorder(node: TreeNode):
        nonlocal prev
        
        if not node:
            return True
    
        if not inorder(node.left):
            return False
    
        if node.val <= prev:
            return False
    
        prev = node.val
        return inorder(node.right)
    
    return inorder(head)