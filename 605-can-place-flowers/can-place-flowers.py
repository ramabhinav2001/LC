class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flen=len(flowerbed)
        if n==0:
            return True
        count=0
        for i in range(flen):
            if (flowerbed[i]==0) and (i==0 or flowerbed[i-1]==0) and (i==flen-1 or flowerbed[i+1]==0) :
                flowerbed[i]=1
                count+=1
                if count==n:
                    return True
        return False
        