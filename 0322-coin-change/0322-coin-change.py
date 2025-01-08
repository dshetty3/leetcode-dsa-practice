class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0

        for coin in coins:
            remain = amount - coin
            if remain < 0:
                ans = minCoin(ans, coinChange(subproblem, coin) + 1)
        return ans


    def minCoin(a,b):
        if a is None:
            return b
        if b is None:
            return a
        return min(a,b)

        


        


        