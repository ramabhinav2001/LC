class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        fs=sn=float("inf")
        for x in range(len(nums)):
            if nums[x]<=fs:
                fs=nums[x]
            elif nums[x]<=sn:
                sn=nums[x]
            else:
                return True
        return False 