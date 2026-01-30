class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_pal(sub):
            return(sub==sub[::-1])
        def bt(i,res):
            if i==len(s):
                ans.append(res)
                return
            for j in range(i+1,len(s)+1):
                if is_pal(s[i:j]):
                    bt(j,res+[s[i:j]])
        ans=[]
        bt(0,[])
        return ans
                