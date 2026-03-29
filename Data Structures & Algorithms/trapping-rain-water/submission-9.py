class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0

        for i in range(len(height)):
            l, mxl, r, mxr = 0, 0, len(height)-1, 0
            while l <= i:
                mxl = max(height[l],mxl)
                l += 1

            while r >= i:
                mxr = max(height[r],mxr)
                r -= 1
            water += min(mxl, mxr) - height[i]
        return water