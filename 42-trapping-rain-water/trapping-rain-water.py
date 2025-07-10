class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        li=0
        ri=len(height)-1
        lmax=height[li]
        rmax=height[ri]
        ans=0
        while li<ri:
            if lmax<rmax:
                li +=1
                lmax=max(lmax,height[li])
                ans +=lmax-height[li]
            else:
                ri -=1
                rmax=max(rmax,height[ri])
                ans +=rmax-height[ri]
        return ans