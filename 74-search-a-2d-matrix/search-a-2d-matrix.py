class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n=len(matrix)
        m=len(matrix[0])
        low=0
        high=n*m-1
        while low<=high:
            mid=(low+high)//2
            x=mid//m
            y=mid%m
            if target==matrix[x][y]:
                return True
            elif target>matrix[x][y]:
                low=mid+1
            else:
                high=mid-1
        return False

