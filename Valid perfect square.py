class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        # Using binary search algorithm 
        left = 1
        right = num

        while left <= right: 

            mid = (left + right)//2

            #If mid^2 is equal to num, return mid 
            if mid*mid == num:
                return mid 
            
            #If mid*mid > num then lower the right index by 1 position from mid
            elif mid*mid > num:
                right = mid - 1 
            
            #If mid*mid < num then increase the left index by 1 position from mid
            else:
                left = mid + 1 

        return False
        
        
        
        '''
        9/70 testcases passed 
        Time limit exceeded

        if num == 1:
            return True
        for i in range(1,(num//2)+1):
            if i*i == num: 
                return True 
        
        return False
        '''
