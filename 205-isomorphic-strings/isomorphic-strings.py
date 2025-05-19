class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        charmaps={}
        charmapt={}
        for i in range(len(s)):
            char1=s[i]
            char2=t[i]
            if char1 in charmaps and charmaps[char1]!=char2 or char2 in charmapt and charmapt[char2]!=char1:
                return False
            charmaps[char1]=char2
            charmapt[char2]=char1
        return True