class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        n=len(s)
        i=0
        sign=1
        while i<n and s[i]==" ":
            i+=1
        if i<n and (s[i]=="-" or s[i]=="+"):
            if s[i]=="-":
                sign=-1
            else:
                sign=1
            i +=1
        ans=0
        while i<n and s[i].isdigit():
            ans=ans*10+int(s[i])
            if ans*sign>2**31 - 1:
                return 2**31 - 1
            if ans*sign<-2**31:
                return -2**31
            i+=1
        return sign*ans


