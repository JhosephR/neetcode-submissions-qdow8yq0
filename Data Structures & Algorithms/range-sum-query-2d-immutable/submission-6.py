class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sum = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]

        for r in range(len(matrix)):
            prefix = 0
            for c in range(len(matrix[0])):
                prefix += matrix[r][c]
                self.sum[r + 1][c + 1] = prefix + self.sum[r][c + 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        bottomRight = self.sum[r2][c2]
        above = self.sum[r1 - 1][c2]
        left = self.sum[r2][c1 - 1]
        topLeft = self.sum[r1 - 1][c1 - 1]

        return bottomRight - above - left + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)