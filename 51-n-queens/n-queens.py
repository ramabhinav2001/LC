class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
            
        def bt(board,ans,n,col,leftrow,lowerleftd,upperleftd):
            if col==n:
                ans.append(["".join(row) for row in board])
                return
            for row in range(n):
                if leftrow[row]==0 and lowerleftd[row+col]==0 and upperleftd[n-1+col-row]==0:
                    board[row][col]="Q"
                    leftrow[row]=1
                    lowerleftd[row+col]=1
                    upperleftd[n-1+col-row]=1
                    bt(board,ans,n,col+1,leftrow,lowerleftd,upperleftd)
                    board[row][col]="."
                    leftrow[row]=0
                    lowerleftd[row+col]=0
                    upperleftd[n-1+col-row]=0

        ans=[]
        board=[["." for _ in range(n)]for _ in range(n)]
        leftrow=[0]*n
        lowerleftd=[0]*(2*n-1)
        upperleftd=[0]*(2*n-1)
        bt(board,ans,n,0,leftrow,lowerleftd,upperleftd)
        return ans