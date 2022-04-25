import math 

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        if math.prod(nums) > 0:
            return 1 
        elif math.prod(nums) == 0: 
            return 0 
        else: 
            return -1 
