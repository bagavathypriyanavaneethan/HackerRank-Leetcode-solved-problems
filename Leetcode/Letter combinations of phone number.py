class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'], 7: ['p', 'q', 'r','s'], 8: ['t', 'u','v'], 9: ['w', 'x','y','z']}

        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return res[int(digits)]
        else:
            final = []
            for i in digits: 
                final.append(res[int(i)])

            lst = [''.join(s) for s in product(*final)]
            return lst 


        
        
