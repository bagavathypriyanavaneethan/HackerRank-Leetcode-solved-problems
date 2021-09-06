class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0 
        buy = prices[0]
        
        for a in prices:
            if a<buy:
                buy = a 
            elif a>buy:
                temp = a-buy
                if temp>profit:
                    profit=temp
        return profit
        
        
        
        '''
        #Time limit exceeded & passed one test case 
        profit = 0 
        
        for i in range(1,len(prices)):
            a = max(prices[i:])-min(prices[0:i])
            if a>profit:
                profit = a 
            
        return profit '''
            
        
