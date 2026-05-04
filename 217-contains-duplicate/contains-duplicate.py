class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        n=len(nums)
        nums.sort()
        x=nums[0]
        for i in range(1,n):
            if x==nums[i]:
                return True
            x=nums[i]
        return False