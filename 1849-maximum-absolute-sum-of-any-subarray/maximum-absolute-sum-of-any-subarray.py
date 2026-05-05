class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        s=0
        mini=0
        maxn=0
        n=len(nums)
        for i in range(n):
            s +=nums[i]
            mini=min(mini,s)
            maxn=max(maxn,s)
        return maxn-mini