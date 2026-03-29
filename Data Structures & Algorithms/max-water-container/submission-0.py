class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mx = 0
        l = 0
        r = len(heights)-1
        d = r

        while l < r:
            amount = min(heights[l],heights[r]) * d
            if amount > mx:
                mx = amount
            if heights[l] < heights[r]:
                l += 1
                d -= 1
            elif heights[l] > heights[r]:
                r -= 1
                d -= 1
            else:
                r -= 1
                d -= 1
        return mx