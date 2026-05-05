class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        cnd=0
        for num in nums:
            if count==0:
                cnd=num
            if num==cnd:
                count +=1
            else:
                count -=1
        return cnd