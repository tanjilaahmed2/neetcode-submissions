class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #two pointer
        maxprofit = 0
        B = 0

        for S in range(1, len(prices)):
            profit = prices[S] - prices[B]
            if profit <=0:
                B = S
            else:
                maxprofit = max(profit, maxprofit)

        return maxprofit        
         

        