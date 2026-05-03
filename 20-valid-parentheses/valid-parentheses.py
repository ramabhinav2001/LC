class Solution:
    def isValid(self, s: str) -> bool:
        st = []
    
        for char in s:
            if char == ')':
                if not st or st.pop() != '(':
                    return False
            elif char == '}':
                if not st or st.pop() != '{':
                    return False
            elif char == ']':
                if not st or st.pop() != '[':
                    return False
            else:
                st.append(char)
        
        return not st
                