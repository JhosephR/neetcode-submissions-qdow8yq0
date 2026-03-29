class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i, v in enumerate(heights):
            h, w = v, 1
            curr_area = h * w
            max_area = max(curr_area, max_area)

            for j in range(i + 1, len(heights)):
                h, w = min(h, heights[j]), w + 1
                curr_area = h * w
                max_area = max(curr_area, max_area)
        return max_area