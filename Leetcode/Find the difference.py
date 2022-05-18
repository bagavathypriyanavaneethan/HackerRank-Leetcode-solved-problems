class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        s_dic = {}
        t_dic = {}
        
        #Frequency of elements in s_dic
        for i in s:
            if i not in s_dic:
                s_dic[i] = 1
            else:
                s_dic[i] +=1
              
        #Frequency of elements in t_dic
        for i in t:
            if i not in t_dic:
                t_dic[i] = 1
            else:
                t_dic[i] +=1
        
        for key,val in t_dic.items():
            #Element that is not available in s_dic
            if key not in s_dic.keys():
                return key
            
            #Element that is available in s_dic, but it appears additionally in s_dic
            elif key in s_dic.keys() and t_dic[key] > s_dic[key]:
                return key
