class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st=[]
        nge={}
        for num in nums2:
            while st and num>st[-1]:
                nge[st.pop()]=num
            st.append(num)
        while st:
            nge[st.pop()]=-1
        
        res=[]
        for num in nums1:
            res.append(nge[num])
        return res