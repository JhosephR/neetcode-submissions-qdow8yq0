class Solution:
    def trap(self, height: List[int]) -> int:
        totalWater, l, r = 0, 0, len(height)-1
        maxL = height[l]
        maxR = height[r]

        while l < r:
            if maxR < maxL:
                r -= 1
                water = maxR - height[r]
                if maxR < height[r]:
                    maxR = height[r]
            else:
                l += 1
                water = maxL - height[l]
                if maxL < height[l]:
                    maxL = height[l]
            if water >= 0:
                totalWater += water
        return totalWater