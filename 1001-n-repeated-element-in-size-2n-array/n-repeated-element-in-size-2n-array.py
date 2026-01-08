class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        return (sum(nums) - sum({*nums})) // (len(nums) // 2-1)