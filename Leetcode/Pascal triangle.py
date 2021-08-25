class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        elif numRows == 2:
            return [[1],[1,1]]
        
        res = [[1],[1,1]]
        
        numRows -= 2
        
        while numRows > 0:
            
            a = [1]
            
            for i in range(0,len(res[-1])-1):
                a.append(res[-1][i]+res[-1][i+1])
                
            a.append(1)
            res.append(a)
        
            numRows-=1
            
        return res
