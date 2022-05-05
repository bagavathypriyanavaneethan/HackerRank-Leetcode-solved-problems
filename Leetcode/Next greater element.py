class Solution:
    def nextGreaterElement(self, A: List[int], B: List[int]) -> List[int]:  
        stack = []
        diff = {}
        
        for pos, val in enumerate(B):
            
            #Checking the current value with the previous value 
            while stack and stack[-1] < val:
                diff[stack.pop()] = val        
                #adding the next greater value to each element in dictionary
            
            #Adding every element to stack for next comparison
            stack.append(val)
            
            #In diff for every element, there is next greater value added 
            
        for pos in range(len(A)):
            if A[pos] in diff:
                A[pos] = diff[A[pos]]
            else:
                A[pos] = -1
                    
        return A
                
            
            
        
