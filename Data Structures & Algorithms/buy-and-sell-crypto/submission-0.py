class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        max_profit = 0

        for price in prices: 
            if price < lowest:
                lowest = price
            
            profit = price - lowest

            if profit > max_profit:
                max_profit = profit

        return max_profit 
            