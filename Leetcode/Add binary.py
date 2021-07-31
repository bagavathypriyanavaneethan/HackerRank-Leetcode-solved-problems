class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        length = max(len(a),len(b))
        carry = 0 
        
        a = a.zfill(length)
        b = b.zfill(length)
        
        for i in range((length)-1,-1,-1):
            r = carry 
            
            r+=1 if a[i]== '1' else 0
            r+=1 if b[i]=='1' else 0 
            
            res = ('1' if r%2==1 else '0') + res
            
            carry = 0 if r<2 else 1
            
        if carry!=0:
            res = '1'+res
        
        return res
            
        
