class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''
        for i in digits:
            num = num + str(i)
        num= str(int(num) + 1)
        res = []
        for i in num:
            res.append(i)
        return res
        
