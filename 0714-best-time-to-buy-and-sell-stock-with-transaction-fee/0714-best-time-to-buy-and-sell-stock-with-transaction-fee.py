class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """

        # pr = 0
        # hold = -prices[0]

        # for price in prices[1:]:
        #     hold = max(hold, pr - price)
        #     pr = max(pr, hold + price - fee)
        # return pr
            
        if len(prices) < 2:
            return 0
        
        profit = 0
        minimum = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            elif prices[i] > minimum + fee:
                profit += prices[i] - minimum - fee
                minimum = prices[i] - fee
        return profit
        