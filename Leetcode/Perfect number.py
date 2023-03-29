class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return False

        res = 1 

        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                res += i + (num/i)

        if res == num:
            return True 

        return False

        '''
        57/98 testcases passed
        Time Limit exceeded
        div = []

        for i in range(1,(num//2)+1):
            if num % i == 0:
                div.append(i)

        if num == sum(div):
            return True 

        return False
        '''
