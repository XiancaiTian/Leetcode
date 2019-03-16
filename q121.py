class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        else:
            low = prices[0]
            profit = 0
            for i, v in enumerate(prices):
                print(v)
                low = min(v, low) # 7 1 - 
                profit = max(v-low, profit) #  0 6 6
            return profit
