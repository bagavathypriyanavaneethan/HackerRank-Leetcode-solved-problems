class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        if len(mat)*len(mat[0]) != r*c:
            return mat 
        
        res = []
        flatten_list = [i for rec in mat for i in rec]
        
        for i in range(r):
            res.append([flatten_list.pop(0) for j in range(c)])
            
        return res
