class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st=[]
        for i in nums1:
            if i not in nums2:
                st.append(-1)
            elif i in nums2:
                x=nums2.index(i)
                if x==len(nums2)-1:
                    st.append(-1)
                for j in range(x+1,len(nums2)):
                    if nums2[x]<nums2[j]:
                        st.append(nums2[j])
                        break
                    if j==len(nums2)-1 and nums2[x]>nums2[j]:
                        st.append(-1)
                    
        return st 