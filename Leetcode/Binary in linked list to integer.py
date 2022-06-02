# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        n = ''
        while head: 
            n = n + str(head.val)
            head = head.next
            
        return int((n),2)
    
    
    '''int(string,base) - converts the no in the string in given base to decimal'''
