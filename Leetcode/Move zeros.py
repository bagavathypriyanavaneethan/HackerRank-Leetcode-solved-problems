class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        ptr = 0 
        for i in range(len(nums)):
            #print(ptr,i,nums[i])
            if nums[i] != 0:
                nums[i],nums[ptr] = nums[ptr],nums[i]
                ptr +=1
                #print(nums)
                
        # Only when the nums[i] != 0 we are moving the pointer 
        # otherwise it will stay same, if the pointer and i are at same position
        # and it's non-zero , swapping will not happen as i = ptr = 1 (same postn)
        # run the code to understand from print statements
        
        '''
        for i in nums:
            print(nums)
            if i == 0:
                nums.remove(i)
                nums.append(0)
				
        return nums
        
        remove - removes the first occurence of the value 
        pop - takes the value of the index mentioned in the method
        '''
