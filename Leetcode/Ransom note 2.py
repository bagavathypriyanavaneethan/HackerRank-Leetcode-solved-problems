import collections
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        res1 = collections.Counter(ransomNote)
        res2 = collections.Counter(magazine)

        res = list(res1-res2)
        if res == []:
            return True 
        else:
            return False
        
