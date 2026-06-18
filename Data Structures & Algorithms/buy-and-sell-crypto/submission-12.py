class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, maxP = 0, 0

        for r in range(1, len(prices)):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(profit, maxP)
            else:
                l = r
        return maxP