# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=None, next=None):

        self.val = val  
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #head = l3 = ListNode(l1.val)
        ls = []
        while l1:
            ls.append(l1.val)
            l1 = l1.next
        while l2:
            ls.append(l2.val)
            l2 = l2.next
        ls.sort()
        #print(ls)
        if len(ls)==1:
            #print('start')
            head = l3 = ListNode(ls.pop(0))
            return head
        if len(ls)>0:
            #print('a')
            head = l3 = ListNode(ls.pop(0))
        else:
            #print('b')
            head = ListNode(val=None)
            return head.next
        if len(ls)>0:
            #print('c')
            for i in ls:
                print('d')
                l3.next = ListNode(i)
                l3 = l3.next
            return head
        
