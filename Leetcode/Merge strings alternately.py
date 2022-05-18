class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = ''
        for i,j in zip(word1,word2):
            res += (i+j)
            
        #When two strings are of same length
        if len(word1) == len(word2):
            return res 
        
        #When word1 is bigger than word2, add the remaining elements
        elif len(word1) > len(word2):
            res += word1[len(word2):]
            return res 
        #When word2 is bigger than word1, add the remaining elements
        elif len(word2) > len(word1):
            res += word2[len(word1):]
            return res
