class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        mapping={
            "{":"}",
            "(":")",
            "[":"]"
        }
        for char in s:
            if char in mapping.values():
                if not st or mapping[st.pop()]!=char:
                    return False
            else:
                st.append(char)
        return not st