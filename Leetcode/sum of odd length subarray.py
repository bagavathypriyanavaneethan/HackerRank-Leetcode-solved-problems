class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        res = []
        for i in range(len(arr)+1):
            for j in range(i):
                #checking whether the length of the subarray is odd
                if len(arr[j:i]) %2 == 1:  
                    res.append(arr[j:i])
                    
        print(res)
        return sum(map(sum,res))
        
        '''
        map(sum,res) will return the list of sum of all subarrays [1,4,7,11,10,15,..]
        so to sum all the sum of subarray again passing that to sum method 
        '''
