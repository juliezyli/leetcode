def maxProfit(self, prices: List[int]) -> int:
        final = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] - prices[i] > 0:
                final += prices[i + 1] - prices[i]
        return final