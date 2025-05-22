class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        hashm={}
        for i in s:
            if i in hashm:
                hashm[i]+=1
            else:
                hashm[i]=1
        b=""
        while hashm:
            max_key=max(hashm,key=hashm.get)
            max_value=hashm.pop(max_key)
            b +=max_key*max_value
        return b
        

