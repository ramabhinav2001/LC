class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0
        maxlen=0
        ch_s=set()
        for end in range(len(s)):
            while s[end] in ch_s:
                ch_s.remove(s[start])
                start +=1
            ch_s.add(s[end])
            maxlen=max(maxlen,end-start+1)
        return maxlen
            
            