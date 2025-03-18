class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        buy1, buy2 = float("inf"), float("inf")
        profit1, profit2 = 0, 0
        for p in prices:
            buy1 = min(buy1, p)
            profit1 = max(profit1, p - buy1)
            buy2 = min(buy2, p - profit1)
            profit2 = max(profit2, p - buy2)
        return profit2
        