class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        else:
            l = len(nums)-1
            i = 0 
            
            while i<l:
                ab = nums.pop(i)
                if ab in nums:
                    nums.remove(ab)
                else:
                    return ab 
                
        '''
        #Maths solution 
        #2(a+b+c)-(a+a+b+b+c+c) => 2a+2b+2c-2a-2b-c = c gives the single value
        return 2*sum(set(nums)) - sum(nums)'''
        
