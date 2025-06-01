class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        r="^#"+"#".join(s)+"#$"
        n=len(r)
        p=[0]*n
        center=right=0
        for i in range(1,n-1):
            mirror=2*center-i
            if i<right:
                p[i]=min(right-i,p[mirror])

            while r[i+p[i]+1]==r[i-(p[i]+1)]:
                p[i]+=1
            if i+p[i]>right:
                center,right=i,i+p[i]
        max_len=max(p)
        center_index=p.index(max_len)
        start=(center_index-max_len)//2
        return s[start:start+max_len]