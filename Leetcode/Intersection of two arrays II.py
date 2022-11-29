class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #return [val for val in nums1 if val in nums2]
        res = []
        for val in nums1: 
            if val in nums2: 
                res.append(val)
                nums2.remove(val)
        return res 
