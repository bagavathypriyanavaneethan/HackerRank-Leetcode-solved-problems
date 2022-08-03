class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s_dic = {}
        #Creating dictionary for s and t string element as key and their no of               #occurence as value
        for i in s: 
            if i not in s_dic: 
                s_dic[i] = 1 
            else: 
                s_dic[i] += 1 
                
        t_dic = {}
        for i in t:
            if i not in t_dic: 
                t_dic[i] = 1
            else: 
                t_dic[i] +=1 
                
        for key,val in s_dic.items():
            if key not in t_dic:
                return False
            if val != t_dic[key]:
                return False 
        return True
        
        '''for i in s_dic.keys():
            #Checking element from s present in t also 
            if i not in t_dic : 
                return False 
            
            #If that is present, checking the no of occurence
            elif s_dic[i] != t_dic[i]:
                return False 
        return True'''
