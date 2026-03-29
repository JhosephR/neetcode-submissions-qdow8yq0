class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # pairs of [index, height]
        max_area = 0

        for r_boundary, r_height in enumerate(heights):
            start = r_boundary
            while stack and r_height < stack[-1][1]:
                l_boundary, l_height = stack.pop()
                max_area = max(max_area, l_height * (r_boundary - l_boundary))
                start = l_boundary
            stack.append([start, r_height])

        for index, height in stack:
            max_area = max(max_area, height * (len(heights) - index))
        
        return max_area