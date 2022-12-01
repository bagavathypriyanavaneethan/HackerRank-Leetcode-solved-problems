# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.guess_res(1,n)
        
    def guess_res(self,low,high):
        mid = (low + high)//2 
        if guess(mid) == 0:
            return mid 
        else:
            return self.guess_res(low,mid-1) if guess(mid) == -1 else self.guess_res(mid + 1,high)
        
