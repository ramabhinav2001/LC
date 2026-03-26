class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==divisor:
            return 1
        if dividend==-2**31 and divisor== -1:
            return (2**31)-1
        if divisor==1:
            return dividend

        n,d=abs(dividend), abs(divisor)
        ans=0
        while n>=d:
            temp=0
            while n>=(d<<temp):
                temp+=1
            temp-=1
            n -=(d<<temp)
            ans +=(1<<temp)
        if (dividend < 0)^(divisor<0):
            return min(max(-ans,-2**31),2**31 -1)
        else:
            return min(max(ans,-2**31),2**31 -1)