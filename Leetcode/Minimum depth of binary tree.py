# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        
        if root is None:
            return 0
        
        if root.left and root.right:
            return min(self.minDepth(root.left),self.minDepth(root.right))+1
        elif root.left is None and root.right:
            return self.minDepth(root.right)+1
        elif root.right is None and root.left:
            return self.minDepth(root.left)+1
        else:
            return 1
        
        '''
        def Depth(node):
            if not node:
                return 0 
            elif root.left and root.right:
                return min(Depth(node.left),Depth(node.right))+1
            
        a = Depth(root.left)
        b = Depth(root.right)
        
        return min(a+1,b+1)'''
        
        
        
