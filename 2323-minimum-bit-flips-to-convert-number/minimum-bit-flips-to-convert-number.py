class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        def tobin(num):
            x=[]
            while(num>=1):
                rem=num%2
                x.append(str(rem))
                num=num//2
            return x
        revy=tobin(start)
        revz=tobin(goal)
        i=0
        l1=len(revy)
        l2=len(revz)

        if l1<l2:
            for i in range(l2-l1):
                revy.append("0")
        if l1>l2:
            for i in range(l1-l2):
                revz.append("0")
        count=0
        l1=len(revy)
        l2=len(revz)
        for i in range(l1):
            if revy[i]!=revz[i]:
                revy[i]=revz[i]
                count +=1
        return count