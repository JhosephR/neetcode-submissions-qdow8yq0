class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1
        while top <= bot:
            row = top + ((bot - top) // 2)
            if matrix[row][0] > target:
                bot = row - 1
            elif matrix[row][-1] < target:
                top = row + 1
            else:
                break
        
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            col = l + ((r - l) // 2)
            if matrix[row][col] < target:
                l = col + 1
            elif matrix[row][col] > target:
                r = col - 1
            else:
                return True
        return False