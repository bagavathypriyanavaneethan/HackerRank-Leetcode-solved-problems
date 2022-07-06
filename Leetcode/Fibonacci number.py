class Solution:
    def fib(self, n: int) -> int:
        
        if n == 0:
            return n 
        elif n == 1:
            return 1 
        
        else: 
            res = [0,1]
            
            for i in range(1,n): 
                res.append(res[-1] + res[-2])
                
            return res[n]
                
        
        
