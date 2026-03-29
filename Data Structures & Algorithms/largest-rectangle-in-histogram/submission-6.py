class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # pairs of [index, height]
        max_area = 0

        for right_i, right_h in enumerate(heights):
            start = right_i
            while stack and right_h < stack[-1][1]:
                    left_i, left_h = stack.pop()
                    max_area = max(max_area, left_h * (right_i - left_i))
                    start = left_i        
            stack.append([start, right_h])
        
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area