class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod=10**9 +7
        nums.sort()
        n=len(nums)
        power=[1]*(n+1)
        for i in range(1,n+1):
            power[i]=(power[i-1]*2) % mod
        left,right=0,n-1
        ans=0
        while left<=right:
            if nums[left]+nums[right]<=target:
                ans=(ans+power[right-left])%mod
                left +=1
            else:
                right -=1
        return ans
