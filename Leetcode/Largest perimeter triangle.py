class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        
        A.sort(reverse = True)
        n = len(A)
        for i in range(0,n-2):
            if A[i+1] + A[i+2] > A[i]:
                return A[i]+A[i+1]+A[i+2]
            
        return 0 
    
    
    '''
    A triangle is valid if sum of its two sides is greater than the third side. 
    Here first we are sorting the array by descending order 
    Then taking the first three sides, and check whether they meet the condition
    eg: 7,10,5
    Order:10,7,5
    then check whether 7+5 > 10 
    and no need to check other combinations as it's sorted in descending order 
    ideally 10+7 > 5 and 10+5 > 7 
    If this is true, we return this perimeter. as the objective is to return the         largest perimeter
    '''
        
