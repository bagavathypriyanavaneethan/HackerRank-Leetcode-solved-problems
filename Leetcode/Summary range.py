class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        temp = []
        for i in range(len(nums)):
            if i+1 <= len(nums)-1 and nums[i] == nums[i+1]-1:
                temp.append(nums[i])
            elif len(temp) == 0 :
                res.append(str(nums[i]))
            else:
                temp.append(nums[i])
                t = str(min(temp))+"->"+str(max(temp))
                res.append(t)
                temp = []
        return res
