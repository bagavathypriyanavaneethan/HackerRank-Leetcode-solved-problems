class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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
                
        #If the dictinaries don't have same size, then return False
        if len(s_dic) != len(t_dic):
            return False
        
        #If they are same size, proceeding
        for i in s_dic.keys():
            #Checking element from s present in t also 
            if i not in t_dic : 
                return False 
            
            #If that is present, checking the no of occurence
            elif s_dic[i] != t_dic[i]:
                return False 
        return True
