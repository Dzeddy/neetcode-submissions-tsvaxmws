class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        l = 0
        r = 1

        profit = 0

        while r < len(prices):
            profit = max(profit, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
            r += 1
        return profit