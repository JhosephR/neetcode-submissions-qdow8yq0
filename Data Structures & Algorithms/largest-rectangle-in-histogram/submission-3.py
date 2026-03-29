class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea, stack = 0, []

        for r_boundary, r_height in enumerate(heights):
            start = r_boundary
            while stack and stack[-1][-1] > r_height:
                l_boundary, l_height = stack.pop()
                maxArea = max(maxArea, l_height * (r_boundary - l_boundary))
                start = l_boundary
            stack.append([start, r_height])

        for index, height in stack:
            maxArea = max(maxArea, height * (len(heights) - index))
        return maxArea