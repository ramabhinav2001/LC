class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsmap={}
        sumn=0
        n=len(nums)
        for i in range(n):
            sub=target-nums[i]
            if sub in numsmap:
                return [numsmap[sub],i]
            numsmap[nums[i]]=i
        return []

