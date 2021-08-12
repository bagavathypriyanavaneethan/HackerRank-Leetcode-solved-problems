# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def Depth(node):
            if not node:
                return 0 
            else:
                return max(Depth(node.left),Depth(node.right))+1
            
        return Depth(root)
        
        '''ls = []
        def Traverse(p):
            
            if p:
                Traverse(p.left)
                
                ls.append(p.val)
            
                Traverse(p.right)
                
            
        
        Traverse(root.left)
        a = len(ls)
        ls = []
        Traverse(root.right)
        b = len(ls)
        
        return max(a,b)'''
