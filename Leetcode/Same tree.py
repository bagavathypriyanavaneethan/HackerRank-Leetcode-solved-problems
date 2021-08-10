# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def traverse(p,q):
            if p and q:
                return p.val == q.val and traverse(p.left,q.left) and traverse(p.right,q.right)
            elif p and not q:
                return False 
            elif q and not p:
                return False
            else:
                return True
            
        return traverse(p,q)
        
