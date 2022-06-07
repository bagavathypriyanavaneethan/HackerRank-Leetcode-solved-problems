# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode],valid: Optional[bool] = False) -> int:
        
        if root.left or root.right:
            res = 0 
            
            if root.left: 
                res += self.sumOfLeftLeaves(root.left,True)
                
            if root.right:
                res += self.sumOfLeftLeaves(root.right)
                
            return res
            
        elif valid:
            return root.val 
        
        else:
            return 0 
        
        return root
        
