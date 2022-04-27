class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        res = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                res.append([s1[i],s2[i]])
         
        #Means the two strings are same 
        if not res:       
            return True 
        
        #Only two diff swap is allowed,so check the no of diff pairs 
        #Then check whether the reverse of one pair is equal to the other pair
        elif len(res) == 2 and res[0][::-1] == res[1]:
            return True 
        return False
        
        '''if s1 == s2: 
            return True 
        
        s2_org = s2 
        for i in range(len(s2)):
            for j in range(len(s2)):
                if i!=j: 
                    s2[i] = s2[j]
                    s2[j] = s2[i]
                    if s2 == s1: 
                        return True 
                    s2 = s2_org 
        return False'''
