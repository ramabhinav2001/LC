class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans=[]
        dtl={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        def lcomb(ind,s):
            if len(s)==len(digits):
                ans.append(s)
                return
            for i in dtl[digits[ind]]:
                lcomb(ind+1,s+i)
        lcomb(0,"")
        return ans
            