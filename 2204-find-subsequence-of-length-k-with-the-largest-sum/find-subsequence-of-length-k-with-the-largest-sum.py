class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        x=[]
        for i in range(len(nums)):
            x.append([i,nums[i]])
        x.sort(key=lambda pair:-pair[1])
        x=x[:k]
        x.sort(key=lambda pair:pair[0])
        return [num for ind,num in x]
        
        

        

