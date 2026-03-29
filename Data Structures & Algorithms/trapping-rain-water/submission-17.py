class Solution:
    def trap(self, height: List[int]) -> int:
        l, r, maxWater = 0, len(height) - 1, 0
        maxl, maxr = height[l], height[r]

        while l < r:
            if maxl < maxr:
                l += 1
                maxl = max(maxl, height[l])
                maxWater += maxl - height[l]
            else:
                r -= 1
                maxr = max(maxr, height[r])
                maxWater += maxr - height[r]
        return maxWater