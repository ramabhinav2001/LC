class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # def isvalid(board, row, col, k):
        #     # Check column
        #     for i in range(9):
        #         if board[i][col] == k:
        #             return False

        #     # Check row
        #     for j in range(9):
        #         if board[row][j] == k:
        #             return False

        #     # Check 3x3 box
        #     boxsrow = 3 * (row // 3)
        #     boxscol = 3 * (col // 3)

        #     for i in range(3):
        #         for j in range(3):
        #             if board[boxsrow + i][boxscol + j] == k:
        #                 return False

        #     return True

        # for i in range(9):
        #     for j in range(9):
        #         if board[i][j] == ".":
        #             for k in map(str, range(1, 10)):
        #                 if isvalid(board, i, j, k):
        #                     board[i][j] = k

        #                     if self.solveSudoku(board):
        #                         return True

        #                     board[i][j] = "."

        #             return False

        # return True
        s="123456789"
        row=[set()for _ in range(9)]
        col=[set()for _ in range(9)]
        box=[set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    val=board[r][c]
                    ind=3*(r//3)+c//3
                    row[r].add(val)
                    col[c].add(val)
                    box[ind].add(val)
        def bt():
            for r in range(9):
                for c in range(9):
                    if board[r][c]==".":
                        for num in s:
                            ind=3*(r//3)+(c//3)
                            if num not in row[r] and num not in col[c] and num not in box[ind]:
                                board[r][c]=num
                                row[r].add(num)
                                col[c].add(num)
                                box[ind].add(num)
                                if bt():
                                    return True
                                board[r][c]="."
                                row[r].remove(num)
                                col[c].remove(num)
                                box[ind].remove(num)
                        return False
            return True
        bt()
