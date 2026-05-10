class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        low=0
        high=n*m-1
        while low<=high:
            mid=(low+high)//2
            x=mid//m
            y=mid%m
            if matrix[x][y]==target:
                return True
            if matrix[x][y]<target:
                low+=1
            else:
                high -=1
        return False

