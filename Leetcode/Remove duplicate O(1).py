class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        nums[:] = sorted(list(set(nums)))
        return len(nums)
