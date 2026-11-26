class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def numBoats(cap):
            boats, curW = 1, 0
            for w in weights:
                curW += w
                if curW > cap:
                    curW = w
                    boats += 1
            return boats
        
        l, r = max(weights), sum(weights)
        ans = r
        while l <= r:
            m = l + (r - l) // 2
            if numBoats(m) <= days:
                ans = min(ans, m)
                r = m - 1
            else:
                l = m + 1
        return ans