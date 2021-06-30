# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
   def addTwoNumbers(self, l1, l2 ,c = 0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a=l1.val
        temp = l1.next

        n=10
        while(temp):
            #print(temp.val)
            a=n*temp.val+a
            n=n*10
            #print(a)
            temp=temp.next
        #print(a)
        b=l2.val
        t=l2.next
        n=10
        while(t):
            b=n*t.val + b
            n=n*10
            t= t.next
        #print(b)
        c=a+b
        #print(c)
        ls=[]
        if c==0:
            ls=[0]
        while(c!=0):
            ls.append(c%10)
            c=c//10
            
        #print('List',ls)
            
        head = l3 = ListNode(ls.pop(0))
        
        for i in ls:
            l3.next = ListNode(i)
            l3=l3.next
            
        return head
        #print(ls)
        #nod = ListNode(4)
        #dummy.next = head
        #nod = dummy
        #nod = ListNode()
        #print(nod.val)
        '''for i in ls:
            l1.val=i
            l1=l1.next
        return l1 '''
            
