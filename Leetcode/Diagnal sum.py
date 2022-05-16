class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        '''
        Add the elements in the primary diagnal (1,1),(2,2)....(i,j) here i=j
        And add elements which are having sum <= len(mat)-1 
        for 3x3 (0,2) & (2,0)  eg: 0+2 = 3-1
        '''
        res = 0 
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i == j or (i+j) == len(mat)-1:
                    res += mat[i][j]
                    
        return res
