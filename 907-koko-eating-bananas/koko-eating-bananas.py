class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def solve(speed):
            totalh=0
            for pile in piles:
                totalh +=(pile+speed-1)//speed
            return totalh<=h

        low=1
        high=max(piles)
        while low<high:
            mid=(low+high)//2
            if solve(mid):
                high=mid
            else:
                low=mid+1
        return low