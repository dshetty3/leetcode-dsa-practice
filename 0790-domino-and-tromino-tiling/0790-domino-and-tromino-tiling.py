class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [1, 2, 5] + [0] * n
        mod = 10 ** 9 + 7
        for i in range(3, n):
            dp[i] = (dp[i - 1] * 2 + dp[i - 3]) % mod
        return dp[n - 1]
        