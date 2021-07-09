class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        a = ''
        print(len(x))
        for i in range(len(x)-1,-1,-1):
            a = a+x[i]
        if a == x:
            return  True 
        else: 
            return False 
        
