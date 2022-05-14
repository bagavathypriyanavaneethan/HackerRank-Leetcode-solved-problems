class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        x1,y1 = coordinates[0]
        x2,y2 = coordinates[1]
        
        #To find every pair of points has same slope
        for x,y in coordinates[2:]:
            if (y2-y1)*(x-x1) != (y-y1)*(x2-x1):   
                return False
            
        return True
        
        '''
        Slope formula (y2-y1)/(x2-x1) = (y-y1)/(x-x1)
        '''
        
        
        '''
        #Sorting the (x,y) coordinates
        coordinates = sorted(coordinates,key = lambda k: [k[1],k[0]])
        
        res = abs( ((coordinates[1][0]-coordinates[0][0])**2 - (coordinates[1][1]-coordinates[0][1])**2)**0.5 )
        
        for i in range(len(coordinates)-1):
            if res != abs( ((coordinates[i+1][0]-coordinates[i][0])**2 - (coordinates[i+1][1]-coordinates[i][1])**2)**0.5 ): 
                
                return False 
        
        return True
        
        Used formula to find distance between two points and check whether all of them are having same distance         inbetween, but that is not applicable for points in straight line (2,4),(2,5) and (2,8). Here these are in same     line but their distance is different
        
        '''
