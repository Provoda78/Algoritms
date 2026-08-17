from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_sum = float('-inf')
        
        def post_order(node: Optional[TreeNode]):
            nonlocal max_sum
            
            if not node:
                return
            
            right = max(post_order(node.right), 0)
            left = max(post_order(node.left), 0)
            
            curret_max = max(node.val + left, node.val + right)
            max_sum = max(curret_max, max_sum)
            

            