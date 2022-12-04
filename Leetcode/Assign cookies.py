class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        res = 0 
        for i in g:
            for j in s:
                if j >= i:
                    res += 1 
                    s.remove(j)
                    break
        return res 
