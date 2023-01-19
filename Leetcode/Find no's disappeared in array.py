class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        return set(range(1,len(nums)+1)) - set(nums)

        #solution 2 
        #for [1,1] it's not working
        '''nums.sort()
        res = []
        for i,num in enumerate(set(nums)):
            print(i+1,num)
            if i+1 != num:
                res.append(i+1)
        return res 
        '''


        '''
        #Time limit exceeding 
        23/33 test cases passed
        res = list(range(1,len(nums)+1))
        nums = set(nums)
        for i in nums:
            if i in res:
                res.remove(i)

        return res '''
