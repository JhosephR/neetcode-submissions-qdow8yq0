class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_l, max_r, maxArea = height[l], height[r], 0

        while l < r:
            if max_l < max_r:
                l += 1
                max_l = max(max_l, height[l])
                maxArea += max_l - height[l]
            else:
                r -= 1
                max_r = max(max_r, height[r])
                maxArea += max_r - height[r]
        return maxArea