class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n=len(nums)
        win_sum=sum(nums[:k])
        max_win_avg=win_sum/float(k)
        for i in range(k,n):
            win_sum +=nums[i]-nums[i-k]
            max_win_avg=max(max_win_avg,win_sum/float(k))
        return max_win_avg