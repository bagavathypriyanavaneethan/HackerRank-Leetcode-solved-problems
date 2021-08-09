# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ls = []
        def traversal(node):
            if node:
                traversal(node.left)
            
                ls.append(node.val)
            
                traversal(node.right)
        traversal(root)
            
        return ls
