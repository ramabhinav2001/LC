class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s=="" and t=="":
            return True
        match=""
        j=0
        for i in range(len(t)):
            if j<len(s) and t[i]==s[j] :
                match +=t[i]
                j +=1
            if match==s:
                return True
        return False