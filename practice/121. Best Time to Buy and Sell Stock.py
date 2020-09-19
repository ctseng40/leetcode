class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        maxpro = 0
        for i in range(0,n-1):
            for j in range (i+1, n):
                maxpro = max(maxpro, prices[j]-prices[i])
                
        return maxpro
