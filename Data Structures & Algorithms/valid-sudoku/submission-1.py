class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            c_row = [s for s in row if s != "."]
            if len(c_row) == len(set(c_row)):
                continue
            return False

        for i in range(0,9):
            c_col = []
            for j in range(0,9):
                if board[j][i] != '.':
                    c_col.append(board[j][i])
            if len(c_col) == len(set(c_col)):
                continue
            return False

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                c_box = []
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        if board[r][c] != '.':
                            c_box.append(board[r][c])
                if len(c_box) == len(set(c_box)):
                    continue
                return False

        return True
        