class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1_cnt={}
        s2_cnt={}

        for i in range(len(s1)):
            s1_cnt[s1[i]]=s1_cnt.get(s1[i],0)+1
            s2_cnt[s2[i]]=s2_cnt.get(s2[i],0)+1
        if s1_cnt==s2_cnt:
            return True
        start=0
        for end in range(len(s1),len(s2)):
            s2_cnt[s2[end]]=s2_cnt.get(s2[end],0)+1
            s2_cnt[s2[start]] -=1
            
            if s2_cnt[s2[start]]==0:
                del s2_cnt[s2[start]]
            start+=1
            if s1_cnt == s2_cnt:
                return True
        return False