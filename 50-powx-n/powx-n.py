class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans=1
        if n<0:
            x=1/x
            n=-n
        while n>0:
            if n%2==1:
                ans=ans*x
                n=n-1
            else:
                n=n/2
                x=x*x
        return ans
        