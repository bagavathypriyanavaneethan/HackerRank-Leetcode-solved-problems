class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            res = 0 
            for i in nums:
                if i<target:
                    res+=1
                elif i>target:
                    break 
            return res 
            
                    
