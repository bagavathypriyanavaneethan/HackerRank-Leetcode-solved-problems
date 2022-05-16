class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        return max(map(sum,accounts))
    
    #map(sum,accounts) gives the sum of the wealth for each customers 
    #max gives the maximum among those wealths
