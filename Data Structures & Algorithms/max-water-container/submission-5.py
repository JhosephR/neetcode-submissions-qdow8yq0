class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r, mxArea = 0, len(heights)-1, 0

        while l < r:
            currArea = (r - l) * min(heights[l],heights[r])
            mxArea = max(mxArea,currArea)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return mxArea