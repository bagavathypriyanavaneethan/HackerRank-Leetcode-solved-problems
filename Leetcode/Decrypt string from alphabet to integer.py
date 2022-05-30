class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        # To create number to alphabet dictionary
        dic = dict(zip(range(1,27),string.ascii_lowercase))
        res = ''
        i,n = 0,len(s)
        
        while i < n:
            if i<len(s)-2 and s[i+2] == '#':
                res = res + dic[int(s[i:i+2])]
                i += 3
            else:
                res = res + dic[int(s[i])]
                i +=1
                
        return res
            
            
