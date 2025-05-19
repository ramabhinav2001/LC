class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        hasd={}
        for i in range(len(s)):
            hasd[s[i]]=hasd.get(s[i],0)+1
            hasd[t[i]]=hasd.get(t[i],0)-1
        for i in hasd.values():
            if i!=0:
                return False
        return True
            
