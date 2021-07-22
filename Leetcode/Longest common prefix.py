class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = strs[0]
        res = ""
        strs.pop(0)
        for i in range(0,len(s)):
            no = 0 
            for j in strs:
                if s[0:i+1] == j[0:i+1]:
                    #print(s[0:i+1])
                    no += 1 
            if no == len(strs):
                print(res)
                res = s[0:i+1]
        return res
