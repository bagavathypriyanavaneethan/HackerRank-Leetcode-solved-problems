class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        '''count = 0 
        count = [count+1 for i in range(low,high+1) if i%2 == 1]
                
        return len(count)'''
        
        return (high-low)//2 + high%2 + low%2 - (high%2 and low%2)
    
    '''
    high-low // 2 = takes the half of the diff between high and low 
    low%2 - gives 1 if low is odd 
    high%2 - gives 1 if high is odd 
    
    '''
