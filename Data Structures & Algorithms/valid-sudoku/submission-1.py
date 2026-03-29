class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowsHash = defaultdict(set)
        colsHash = defaultdict(set)
        squaresHash = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rowsHash[r] or
                    board[r][c] in colsHash[c] or
                    board[r][c] in squaresHash[(r//3,c//3)]):
                    return False
                rowsHash[r].add(board[r][c])
                colsHash[c].add(board[r][c])
                squaresHash[(r//3,c//3)].add(board[r][c])
        return True