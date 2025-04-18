class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """

        if not prices: return 0
        dp = [0] * len(prices)

        for t in range(k):
            pos = -prices[0]
            pr = 0
            for i in range(len(prices)):
                pos = max(pos, dp[i] - prices[i])
                pr = max(pr, pos + prices[i])
                dp[i] = pr
        return dp[-1]
        