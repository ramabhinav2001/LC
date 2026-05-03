class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        st = []

        for i in range(2 * n):
            while st and nums[i % n] > nums[st[-1]]:
                idx = st.pop()
                res[idx] = nums[i % n]
            
            if i < n:
                st.append(i)
        
        return res