class Solution:
    def toLowerCase(self, s: str) -> str:
        
        # Using bit manipulation 
        # By adding | 32, string will convert to lowercase 
        
        for i in range(len(s)):
            if 65 <= ord(s[i]) <= 90:   # checking the range of upper case 65-90
                x = chr( ord(s[i]) | 32)
                s = s[:i] + x + s[i+1:]
        
        return s 
    
        #ord() - gives unicode no for character 
        #chr() - gives character for unicode number
        
        '''
        Using dictionary
        dic = dict(zip(string.ascii_uppercase,string.ascii_lowercase))
        
        return ''.join(dic.get(i,i) for i in s)
        '''
        
        
        '''
        One line solution
        return s.lower()
        '''
