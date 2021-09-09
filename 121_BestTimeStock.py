class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn,output = 0,0
        for i in range(1,len(prices)):
            if prices[i] < prices[minn]:
                minn = i
            else:
                output = max(output,prices[i]-prices[minn])
        return output