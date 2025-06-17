class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        ans=[1]*n
        pref,suff=1,1
        for i in range(n):
            ans[i]*=pref
            pref*=nums[i]
            ans[-1-i]*=suff
            suff*=nums[-1-i]
        return ans
            