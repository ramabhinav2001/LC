class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        cnt_max=-1
        result_row=-1
        for i, row in enumerate(mat):
            cnt_ones = row.count(1)
            if cnt_ones > cnt_max:
                cnt_max = cnt_ones
                result_row = i
        return [result_row, cnt_max]
            