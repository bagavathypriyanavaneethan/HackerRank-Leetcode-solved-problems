class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        else:
            curr = glob = nums[0]
            
            for i in range(1,len(nums)):
                curr = max(nums[i],curr+nums[i])
                
                if curr > glob:
                    glob = curr 
                    
            return glob 
