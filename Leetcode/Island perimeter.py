class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0 
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1: 
                    res +=4

                    #To check next element
                    if j+1 <= len(grid[i])-1: 
                        if grid[i][j+1] == 1:
                            res -=2
                            

                    #To check above element
                    if i-1 >=0 and i-1 <= len(grid)-1:
                        if grid[i-1][j] == 1:
                            res-=2
                            
        
        return res
