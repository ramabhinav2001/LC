class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans,ds=[], []
        def findcomb(ind,candidates, target, ans, ds):
            if ind==len(candidates):
                if target==0:
                    ans.append(list(ds))
                return
            if candidates[ind]<=target:
                ds.append(candidates[ind])
                findcomb(ind,candidates,target-candidates[ind],ans,ds)
                ds.pop()
            findcomb(ind+1,candidates,target,ans,ds)
        findcomb(0,candidates,target,ans,ds)
        return ans