class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        #Using list comprehension
        ans = [nums[nums[i]] for i in range(len(nums))]
        return ans

        #Using for loop
        '''ans = []

        for i in range(0,len(nums)):
            ans.append(nums[nums[i]])

        return ans'''
            
