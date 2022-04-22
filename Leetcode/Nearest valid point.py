class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        res = 10e4
        result_point = -1
        for i in range(len(points)-1,-1,-1):
            if points[i][0] == x or points[i][1] == y:
                dis = abs(x-points[i][0]) + abs(y-points[i][1])
                
                if dis <= res: 
                    res = dis 
                    result_point = i 
                    
        return result_point 
    
    '''
    In the for loop, traversing in reverse order in order to find the point with           minimum index if two points has same manhattan distance.
    '''
        
