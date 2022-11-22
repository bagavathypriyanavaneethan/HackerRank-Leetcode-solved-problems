class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        
        '''a = int("{0:b}".format(x))
        b = int("{0:b}".format(y))
        print(a,b)
        print(a^b)
        return (str(a^b).count('1'))'''

        res = x^y 
        return bin(res).count('1')
