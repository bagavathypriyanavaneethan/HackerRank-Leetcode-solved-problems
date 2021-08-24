# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False
        
        #Checking while at the leaf node whether the targetsum reaches 0(as values are deduced from target)
        if not root.left and not root.right and targetSum - root.val == 0:
            return True 
        
        #Looping at the right & left side of root and returns true once either of them reaches the target
        return self.hasPathSum(root.right,targetSum-root.val) or self.hasPathSum(root.left,targetSum-root.val)
            
