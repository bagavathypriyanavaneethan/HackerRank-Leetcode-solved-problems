class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        '''if s == " ":
            return 0
        elif len(s)==1:
            return 1
        else:
            res = 0 
            for i in range(len(s)-1,-1,-1):
                if s[i]!=" ":
                    res+=1
                elif s[i]==" ":
                    return res'''
        if not (s and s.strip()):
            return 0
        else:
            res = s.split()
            return len(res[-1])
            
                
        
