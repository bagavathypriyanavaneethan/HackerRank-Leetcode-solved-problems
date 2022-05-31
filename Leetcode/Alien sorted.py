class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        dic = {}
        index = []
        
        for pos,charac in enumerate(order):
            dic[charac] = pos 
            
        for word in words:
            ind = []
            for i in word:
                ind.append(dic[i])
            index.append(ind)
        
        for i in range(len(index)-1): 
            if index[i] > index[i+1]:
                return False 
            
        return True
            
        
