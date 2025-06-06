class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_can=max(candies)
        n=len(candies)
        result=[]
        for i in range(n):
            if candies[i]+extraCandies>=max_can:
                result.append(True)
            else:
                result.append(False)
        return result