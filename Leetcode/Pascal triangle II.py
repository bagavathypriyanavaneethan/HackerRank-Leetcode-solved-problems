class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        a = 1 
        res = [a]
        
        for i in range(rowIndex):
            
            a = a*(rowIndex-i)//(i+1)
            
            res.append(a)
            
        return res
    
    '''
when rowIndex=5: return [1, 5, 10, 10, 5, 1]
Iterative:
1x1/1 =1
1x5/1 = 5
5x4/2 = 10
10x3/3 = 10
10x2/4 = 5
5x1/5 = 1
    '''
