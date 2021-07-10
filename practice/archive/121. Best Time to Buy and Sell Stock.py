# One Pass
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        buy = prices[0]
        temp = 0
        
        for price in prices[1:]:
            if price < buy:
                buy = price;
            else:
                temp = price - buy
                if temp > profit:
                    profit = temp
        print(buy)
        return profit
