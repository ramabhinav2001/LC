class Solution:
    MOD=10**9 + 7
    def pow(self,base,exp):
        result=1
        while exp>0:
            if exp & 1:
                result=(result*base)%self.MOD
            base=(base*base)%self.MOD
            exp >>=1
        return result
    def countGoodNumbers(self, n: int) -> int:
        even_pos=(n+1)//2
        odd_pos=n//2
        return self.pow(5,even_pos)*self.pow(4,odd_pos) % self.MOD
                    