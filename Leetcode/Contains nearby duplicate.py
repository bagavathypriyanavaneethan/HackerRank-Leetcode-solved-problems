class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        seen_val = {}
        
        for i,val in enumerate(nums):
            if val in seen_val:
                if abs(seen_val[val]-i) <= k:
                    return True 
            seen_val[val] = i 
        return False
        
        
        
        '''
        Time limit exceeded 
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j] and abs(i-j) <= k:
                    return True
        
        return False
        
        '''
