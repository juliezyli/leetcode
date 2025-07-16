def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit
    
    # inefficient solution
    #     final = []
    #     if len(prices) < 2:
    #         return 0
    #     for i in range(len(prices) - 1):
    #         final.append(self.helper(prices[i:]))
    #     if max(final) <= 0:
    #         return 0
    #     return max(final)
    # def helper(self, prices):
    #     buy = prices[0]
    #     sell = max(prices[1:])
    #     return int(sell) - int(buy)