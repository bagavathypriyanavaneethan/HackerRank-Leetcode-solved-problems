class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1 :
            return True 
        if n <= 0:
            return False
        while True:
            if n %2 == 0:
                n /= 2 
            elif n%3 == 0:
                n /= 3 
            elif n%5 == 0:
                n /= 5
            elif n == 1:
                return True 
            else:
                return False 
        
        
        '''
        Time Limit exceeded 516/1013 testcases passed
        if n == 1 :
            return True 
        if n <= 0:
            return False
        res = []
        num = 2 
        while n>1:
            if n % num == 0:
                if num not in res:
                    res.append(num)
                n = n/num
            else:
                num = num +1 
        for i in res:
            if i not in (2,3,5):
                return False 
        return True'''
        
