"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# Pre-order traversal: Center,Left,Right
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ls = []
        
        def traversal(node):
            if node:
                ls.append(node.val)
            
                for i in node.children:
                    traversal(i)
            
        traversal(root)
        return ls
        
    '''
    Adding the node value to the list if exists 
    Then traverse throught the node's children if any.
    Return the final list
    '''
