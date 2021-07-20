class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0 and len(haystack)==0:
            return 0 
        if len(haystack)==0 and len(needle)!=0:
            return -1
        if len(haystack)!=0 and len(needle)==0: 
            return 0 
        for i in range(0,len(haystack)):
            if len(needle)!=0 and needle[0] not in haystack:
                return -1
            if len(needle)!=0 and haystack[i] == needle[0]:
                match = 0 
                ind = i 
                print("start")
                for j in range(0,len(needle)):
                    
                    if ind<=len(haystack)-1 and j<=len(haystack)-1 and haystack[ind]==needle[j]:
                        match+=1
                        print(ind,match)
                    elif ind<=len(haystack)-1 and j<=len(haystack)-1 and haystack[ind]!=needle[j]:
                        break
                    ind+=1 
                    
                if match == len(needle):
                    return i 
                elif needle in haystack:
                    return haystack.index(needle)
                else:
                    return -1
        
                
                
        
