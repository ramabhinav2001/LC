class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq={}
        ans=0
        start=0

        for end in range(len(s)):
            freq[s[end]]=freq.get(s[end],0)+1
            maxfreq=max(freq.values())
            curlen=end-start+1
            if curlen-maxfreq>k:
                freq[s[start]] -=1
                start+=1
            ans=max(ans,end-start+1)
        return ans