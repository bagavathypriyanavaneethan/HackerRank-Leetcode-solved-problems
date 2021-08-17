# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)
        left_height = root.left.val if root.left else 0
        right_height = root.right.val if root.right else 0
        print(left_height,right_height)
        root.val = max(left_height, right_height) + 1
        return False if abs(left_height-right_height) > 1 else (left and right)
    
    '''def Depth(self,node):
            
            if not node:
                return 0 
            else:
                print(node.val)
                return max(self.Depth(node.left),self.Depth(node.right))+1
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        
            

                
        if not root:
            return True
        
            
        lef = self.Depth(root.left)
        print("right")
        righ = self.Depth(root.right)
        
        print(lef,righ)
        
        if lef==righ:
            return True
        elif lef+1 == righ:
            return True
        elif righ+1 == lef:
            return True
        else:
            return False'''
        
