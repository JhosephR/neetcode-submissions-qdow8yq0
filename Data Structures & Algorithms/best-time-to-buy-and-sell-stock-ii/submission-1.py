class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = [] #monotonic increasing
        maxProfit = 0

        for i, p in enumerate(prices):
            if stack and stack[-1] > p:
                if prices[i - 1] != p and len(stack) > 1:
                    maxProfit += stack[-1] - stack[0]
                    stack = []
                else:
                    stack.pop()
            stack.append(p)

        maxProfit += stack[-1] - stack[0]
        return maxProfit