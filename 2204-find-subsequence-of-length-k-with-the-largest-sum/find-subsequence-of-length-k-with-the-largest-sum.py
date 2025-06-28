class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        x=[]
        for i in range(len(nums)):
            x.append([nums[i],i])
        x.sort(key=lambda pair:-pair[0])
        x=x[:k]
        x.sort(key=lambda pair:pair[1])
        return [num for num,ind in x]
        
        

        

