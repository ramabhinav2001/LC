class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        mapping={
            ")":"(",
            "}":"{",
            "]":"["
        }

        for char in s:
            if char in mapping.keys():
                if not st or mapping[char]!=st.pop():
                    return False
            elif char in mapping.values():
                st.append(char)
        return not st
