class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        return prod(list(map(int,str(n)))) - sum(list(map(int,str(n))))
    
        '''sum = 0
        product = 1 
        
        for i in str(n): 
            sum += int(i)
            product *= int(i)
            
        print(product,sum)
        return product - sum'''
