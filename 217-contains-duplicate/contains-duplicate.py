class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        x=nums[0]
        for i in range(1,len(nums)):
            if x==nums[i]:
                return True
            x=nums[i]
        return False