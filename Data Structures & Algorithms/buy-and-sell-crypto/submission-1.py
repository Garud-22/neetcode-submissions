class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        if len(prices) == 1:
            return res
        
        min_buy_price = prices[0]
        sell_day = 1
        while sell_day < len(prices):
            min_buy_price = min(min_buy_price, prices[sell_day - 1])
            profit = prices[sell_day] - min_buy_price
            res = max(res, profit)
            sell_day += 1
        return res