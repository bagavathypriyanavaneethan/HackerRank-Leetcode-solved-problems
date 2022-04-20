class Solution:
    def hammingWeight(self, n: int) -> int:
        
        n = format(n,"b")
        print(n)
        return n.count('1')
