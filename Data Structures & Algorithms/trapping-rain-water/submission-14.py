class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_l, max_r, maxArea = l, r, 0

        while l < r:
            if height[max_l] < height[max_r]:
                l += 1
                if height[max_l] < height[l]:
                    max_l = l
                maxArea += height[max_l] - height[l]
            else:
                r -= 1
                if height[max_r] < height[r]:
                    max_r = r
                maxArea += height[max_r] - height[r]
        return maxArea