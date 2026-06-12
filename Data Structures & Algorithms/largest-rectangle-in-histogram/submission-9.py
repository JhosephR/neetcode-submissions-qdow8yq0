class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        mxArea = 0

        for right_i in range(len(heights)):
            start = right_i
            while stack and stack[-1][0] > heights[right_i]:
                left_h, left_i = stack.pop()
                mxArea = max(mxArea, left_h * (right_i - left_i))
                start = left_i
            stack.append([heights[right_i], start])

        for h, i in stack:
            mxArea = max(mxArea, h * (len(heights) - i))
        return mxArea