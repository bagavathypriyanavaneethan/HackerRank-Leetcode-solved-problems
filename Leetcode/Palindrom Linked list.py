# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        l1 = head 
        a=''
        while(l1):
            a=a+str(l1.val)
            l1=l1.next
        b=''
        for i in range(len(a)-1,-1,-1):
            b=b+a[i]
        #print(b)
        
        if a == b:
            return True
        else:
            return False
