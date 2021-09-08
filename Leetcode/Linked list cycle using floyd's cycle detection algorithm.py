# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        
        #Floyd's cycle finding algorithm
        slow = head
        fast = head
        
        while slow and fast and fast.next: 
            slow = slow.next #Moving node by 1 
            fast = fast.next.next #Moving node by 2 
        
            #When these two nodes meet, they are in loop         
            if slow == fast:
                return True
            
        return False
        
        '''
        #Solved one test case but the problem here is 
        #it will return True if any elements repeats thinking that it forms a cycle
        ls = []
        while head:
            print(head.val)
            if head.val in ls:
                return True
            ls.append(head.val)
            
            head = head.next
            
        return False
        '''
