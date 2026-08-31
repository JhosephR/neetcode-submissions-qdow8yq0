class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (index, height)
        largest = 0
        for r, rh in enumerate(heights):
            start = r
            while stack and stack[-1][1] > rh:
                l, lh = stack.pop()
                area = lh * (r - l)
                largest = max(largest, area)
                start = l
            stack.append((start, rh))
            
        for i, h in stack:
            area = h * (len(heights) - i)
            largest = max(largest, area)
        return largest