class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        num1 = list(num1)
        num2 = list(num2)

        var = 0 
        res = ""

        while num1 or num2 or var: 
            if num1:
                var += int(num1.pop())
            if num2: 
                var += int(num2.pop()) 

            res += str(var%10)
            var //=10 
        return res[::-1]


        #return str(int(num1)+int(num2))
