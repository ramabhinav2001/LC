class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans,ds=[],[]
        def findcomb(ind,candidates, target, ans, ds):
            if target==0:
                ans.append(list(ds))
                return
            for i in range(ind,len(candidates)):
                if i>ind and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>target:
                    break
                ds.append(candidates[i])
                findcomb(i+1,candidates,target-candidates[i],ans,ds)
                ds.pop()

        findcomb(0,candidates,target,ans,ds)
        return ans