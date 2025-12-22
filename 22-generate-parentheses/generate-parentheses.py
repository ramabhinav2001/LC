class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        i=[]
        def rbt(open1,close1):
            if len(i)==2*n:
                res.append("".join(i))
            
            if open1 < n:
                i.append("(")
                rbt(open1+1,close1)
                i.pop()
            if open1>close1:
                i.append(")")
                rbt(open1,close1+1)
                i.pop()
        rbt(0,0)
        return res
            
                
            

                        
