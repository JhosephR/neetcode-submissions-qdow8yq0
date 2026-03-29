class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, bestP = 0, 0

        for r in range(1, len(prices)):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                bestP = max(bestP, profit)
            else:
                l = r
            r += 1
        return bestP