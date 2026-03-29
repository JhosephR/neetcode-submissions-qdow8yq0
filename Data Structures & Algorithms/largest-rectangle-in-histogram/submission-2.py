class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, maxArea = [], 0

        for right_boundary, right_h in enumerate(heights):
            start = right_boundary
            while stack and stack[-1][1] > right_h:
                left_boundary, left_h = stack.pop()
                maxArea = max(maxArea, left_h * (right_boundary - left_boundary))
                start = left_boundary
            stack.append([start, right_h])

        for index, height in stack:
            maxArea = max(maxArea, height * (len(heights) - index))
        return maxArea