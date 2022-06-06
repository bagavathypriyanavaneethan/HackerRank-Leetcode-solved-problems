# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = fast = head 
        
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
            
        return slow
    
    '''Fast moves at a 2X speed
    Slow moves at 1x speed
    So when fast reaches end of list
    Slow is still at the middle of the list'''
        
    '''ls = []
        while head: 
            ls.append(head) #Instead of adding head.val adding the entire node there
            head = head.next
        
        return ls[len(ls)//2]'''
