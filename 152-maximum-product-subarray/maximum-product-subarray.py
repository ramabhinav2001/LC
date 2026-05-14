class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        cmax=nums[0]
        maxs=nums[0]
        cmin=nums[0]
        start=0
        end=0
        t_start=0
        for i in range(1,len(nums)):
            if nums[i]<0:
                cmax,cmin=cmin,cmax
            if cmax*nums[i]<nums[i]:
                cmax=nums[i]
                t_start=i
            else:
                cmax *= nums[i]
            cmin=min(nums[i],nums[i]*cmin)
            if cmax>maxs:
                maxs=cmax
                start=t_start
                end=i
        return maxs