class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mx, l, d = 0, 0, len(heights)
        r = d - 1

        while l < r:
            d -= 1
            amount = min(heights[l],heights[r]) * d
            if amount > mx:
                mx = amount
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                r -= 1
        return mx