# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ls = []
        while(head):
            if head.val not in ls:
                ls.append(head.val)
            head=head.next
        
        #For getting the first element & add to the list
        if len(ls)>0:  
            res = head = ListNode(ls.pop(0))
        
        #If there is not element, then add val as None
        else:
            head = ListNode(val = None)
            return head.next
        
        #Adding the rest of the elements in list if there is 
        if len(ls)>0:
            for i in ls:
                res.next = ListNode(i)
                res = res.next
            return head
        
        #If there was only one element in list & that was added, so return that 
        else:
            return head
            
        
