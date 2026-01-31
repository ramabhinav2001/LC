class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(board,ans,n,row,col):
            for i in range(row):
                if board[i][col] == 'Q':
                    return False

            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            return True
            
        def bt(board,ans,n,row):
            if row==n:
                ans.append(["".join(col) for col in board])
                return
            for col in range(n):
                if is_safe(board,ans,n,row,col):
                    board[row][col]="Q"
                    bt(board,ans,n,row+1)
                    board[row][col]="."
        ans=[]
        board=[["." for _ in range(n)]for _ in range(n)]
        bt(board,ans,n,0)
        return ans