class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows * cols - 1
        while l <= r:
            m = l + ((r - l) // 2)
            num = matrix[m // cols][m % cols]
            if num > target:
                r = m - 1
            elif num < target:
                l = m + 1
            else:
                return True
        return False