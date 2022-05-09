class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        
        freq = {}
        
        for i in set(nums): 
            freq[i] = nums.count(i)
            
        for key,val in freq.items(): 
            if val > len(nums)/2:
                return key
        
        '''
        return max(nums,key=nums.count)
        
        One line solution: It works faster for short lists 
        and time limit exceeded for large list
        '''
