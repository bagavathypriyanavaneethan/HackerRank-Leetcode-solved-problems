class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        #res = False
        comb = []
        for i in range(0,(len(s)//2)+1):
            comb.append(s[0:i])

        for i in comb[1:]:
            if s == i*(len(s)//len(i)):
                return True
        return False
