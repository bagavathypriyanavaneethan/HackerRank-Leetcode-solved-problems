class Solution:
    def sum_of_square(self,n:int):
        res = 0 
        
        while n!=0: 
            res += (n%10)**2 
            n = n//10 
        return res
    
    
    def isHappy(self, n: int) -> bool:
        if n == 1: 
            return True 
        
        num = set()
        while n not in num: 
            num.add(n)
            n = self.sum_of_square(n)  #To find sum of squares of a number
            if n == 1: 
                return True 
        return False
            
'''
1. Find the sum of square of digits of a number 
2. If that result is 1 then return True 
3. Else add that number to set num
4. If the n repeats (means already in set) then return false 
set is faster than list in this case as set is applicable here (because unique elements is enough to check)
'''
