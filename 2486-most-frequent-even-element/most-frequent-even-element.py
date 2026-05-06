class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        hashm={}
        ans=-1
        count=0
        for i in range(len(nums)):
            hashm[nums[i]]=hashm.get(nums[i],0)+1
        for n,c in hashm.items():
            if ans>n and c==count and n%2==0:
                ans=n
            elif c>count and n%2==0:
                ans=n
                count=c
        return ans        