class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """

        # coins.sort()

        # def dfs(i, amount):
        #     if i >= len(coins):
        #         return 0
            
        #     if amount == 0:
        #         return 1
            
        #     res = 0
        #     if amount >= coins[i]:
        #         res = dfs(i + 1, amount)
        #         res += dfs(i, amount - coins[i])
        #     return res
        
        # return dfs(0, amount)


        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            for a in range(1, amount + 1):
                dp[a] += dp[a - coins[i]] if coins[i] <= a else 0
        return dp[amount]


        