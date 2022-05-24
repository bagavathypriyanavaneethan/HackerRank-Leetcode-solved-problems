class Solution:
    def toLowerCase(self, s: str) -> str:
        
        dic = dict(zip(string.ascii_uppercase,string.ascii_lowercase))
        
        return ''.join(dic.get(i,i) for i in s)
        
        
        '''
        One line solution
        return s.lower()
        '''
