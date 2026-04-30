class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in range(len(s)):
            if st:
                top=st[-1]
                if self.is_pair(top,s[i]):
                    st.pop()
                    continue
            st.append(s[i])
        return not st
    def is_pair(self,top,curr):
        if top=="(" and curr==")" or top=="{" and curr=="}" or top=="[" and curr=="]":
            return True
        return False