class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        ans = r
        while l <= r:
            m = l + (r - l) // 2
            if m * m < x:
                ans = m
                l = m + 1
            elif m * m > x:
                r = m - 1
            else:
                return m
        return ans