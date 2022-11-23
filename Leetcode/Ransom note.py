class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = {}
        magzn = {}
        res = False 
        for i in ransomNote:
            ransom[i] = ransom.get(i,0) + 1 
        for j in magazine:
            magzn[j] = magzn.get(j,0) + 1 
        print(ransom,magzn)

        for i in ransom.keys():
            if i in magzn.keys():
                if ransom[i] <= magzn[i]:
                    res = True 
                else:
                    return False
            else:
                return False 
        return res
