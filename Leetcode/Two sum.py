class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j = 0,len(numbers)-1
        
        while numbers[i]+numbers[j] != target:
            if numbers[i] + numbers[j] > target:
                j-=1
            else:
                i+=1
        else:
            return [i+1,j+1]
        
        
        
        
        '''for i in range(0,len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[j] == target - numbers[i]:
                    return [(i+1),(j+1)]'''
