class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanN={'I': 1, 'V': 5, 'X': 10, 'L': 50,'C': 100, 'D': 500, 'M': 1000}
        res=0
        for i in range(len(s)):
            if i+1<len(s) and romanN[s[i]]<romanN[s[i+1]]:
                res -=romanN[s[i]]
            else:
                res +=romanN[s[i]]
        return res
            
        