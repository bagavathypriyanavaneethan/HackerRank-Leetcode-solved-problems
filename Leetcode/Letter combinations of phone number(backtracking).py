class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl", 
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        combinations = []

        def Combination(index,currentString):

            if index == len(digits):
                combinations.append(currentString)
            else:
                for letter in phone[digits[index]]:
                    Combination(index+1,currentString + letter)

        Combination(0,'')
        return combinations        

