class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr=[]
        l=len(nums)
        def bt(arr,temp,nums,start):
            arr.append(temp.copy())
            for i in range(start,l):
                temp.append(nums[i])
                bt(arr,temp,nums,i+1)
                temp.pop()
        bt(arr,[],nums,0)
        return arr