class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                low +=1
            else:
                high -=1
        if low>high:
            return -1
        return low