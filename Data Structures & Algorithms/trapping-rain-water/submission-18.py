class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        mxl, mxr, water = height[l], height[r], 0

        while l < r:
            if mxl < mxr:
                l += 1
                mxl = max(mxl, height[l])
                water += mxl - height[l]
            else:
                r -= 1
                mxr = max(mxr, height[r])
                water += mxr - height[r]
        return water