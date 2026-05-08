class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        minprice=prices[0]

        for i in range(1,len(prices)):
            maxprofit=max(maxprofit,prices[i]-minprice)
            minprice=min(minprice,prices[i])
        return maxprofit
