class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, maxArea = [], 0

        for r_index, r_height in enumerate(heights):
            start = r_index
            while stack and stack[-1][1] > r_height:
                l_index, l_height = stack.pop()
                maxArea = max(maxArea, l_height * (r_index - l_index))
                start = l_index
            stack.append([start, r_height])

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea  