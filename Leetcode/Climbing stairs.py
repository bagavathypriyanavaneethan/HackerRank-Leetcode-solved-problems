class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2 
        else:
            ls = [1]*n
            ls[0]=1
            ls[1]=2
            for i in range(2,n):
                ls[i] = ls[i-1]+ls[i-2]
                
            return ls[n-1]
        
            
            
