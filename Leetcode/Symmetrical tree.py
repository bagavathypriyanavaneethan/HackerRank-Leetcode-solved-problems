# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def traverse(p,q):
            
            if p and q:
                return p.val == q.val and traverse(p.left,q.right) and traverse(p.right,q.left)
            
            elif p and not q:
                return False
            
            elif q and not p:
                return False
            
            else:
                return True
            
        return traverse(root.left,root.right)
        
        '''ls = []
        
        def traverse(node):
            if node:
                
                traverse(node.left)
                ls.append(node.val)
                traverse(node.right)
                
        traverse(root)
        print(ls)
        
        if len(ls)%2 == 0:
            return False 
        
        else:
            a = ls[0:(len(ls)//2)]
            b = ls[len(ls)//2 + 1::]
            
            b.reverse()
            print('b',b)
            no = 0
            for i,j in zip(a,b):
                if i == j:
                    no+=1
                else:
                    return False
            print(no,len(a),len(b))
            if no == len(a):
                return True'''
            
        
