class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """

        pr = 0
        hold = -prices[0]

        for price in prices[1:]:
            hold = max(hold, pr - price)
            pr = max(pr, hold + price - fee)
        return pr
            
        