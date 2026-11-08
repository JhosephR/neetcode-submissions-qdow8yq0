class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        q = deque() #monotonic increasing
        maxProfit = 0

        for i, p in enumerate(prices):
            if q and q[-1] > p:
                if prices[i - 1] != p and len(q) > 1:
                    a, b = q.popleft(), q.pop()
                    maxProfit += b - a
                    q = deque()
                else:
                    q.pop()
            q.append(p)

        maxProfit += q[-1] - q[0]
        return maxProfit