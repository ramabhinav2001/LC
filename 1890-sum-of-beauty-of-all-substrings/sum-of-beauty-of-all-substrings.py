class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        n=len(s)
        for i in range(n):
            freq={}
            freq[s[i]]=freq.get(s[i],0)+1
            for j in range(i+1,n):
                freq[s[j]]=freq.get(s[j],0)+1
                if len(freq)>1:
                    res +=max(freq.values())-min(freq.values())
        return res