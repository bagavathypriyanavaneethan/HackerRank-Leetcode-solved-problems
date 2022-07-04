import string 

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber: 
            columnNumber, r = divmod(columnNumber-1,26)
            res = chr(ord("A")+r) + res 
            print(res)
            
        return res 
            
        
        '''res = dict(zip(range(1,27),string.ascii_uppercase))
        print(res)
        
        if columnNumber <= 26: 
            return res.get(columnNumber)'''
        
