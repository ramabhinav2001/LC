class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        A="("
        B=")"
        real_s=""
        count=0
        for i in range(len(s)):
            if s[i]==A:
                if count>0:
                    real_s +=s[i]
                count+=1
            elif s[i]==B:
                count -=1
                if count>0:
                    real_s +=s[i]
        return real_s
            