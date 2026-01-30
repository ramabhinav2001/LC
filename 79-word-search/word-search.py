class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def bt(i,j,k):
            if k==len(word):
                return True
            if i>=len(board) or i<0 or j>=len(board[0]) or j<0 or board[i][j] != word[k]:
                return False

            temp=board[i][j]
            board[i][j]=""

            if bt(i+1,j, k+1) or bt(i-1,j,k+1) or bt(i,j+1,k+1) or bt(i,j-1,k+1):
                return True

            board[i][j]=temp
            return False
        m=len(board)
        n=len(board[0])
        for i in range(m):
            for j in range(n):
                if bt(i,j,0):
                    return True
        return False