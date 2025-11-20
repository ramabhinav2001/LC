class Solution:
    MOD=10**9 + 7
    def pow(self,base,exp):
        if exp==0:
            return 1
        half=self.pow(base,exp//2)
        half=(half*half)%self.MOD
        if exp%2==1:
            return (base*half) % self.MOD
        return half
    def countGoodNumbers(self, n: int) -> int:
        even_pos=(n+1)//2
        odd_pos=n//2
        return self.pow(5,even_pos)*self.pow(4,odd_pos) % self.MOD
                    