class Solution(object):
    def minExtraChar(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """
        

        dp = [0] * (len(s) + 1)
        dictionarySet = set(dictionary)

        for i in range(len(s) - 1, -1, -1):
            dp[i] = dp[i + 1] + 1
            for w in dictionarySet:
                if (i + len(w) <= len(s) and s[i: i + len(w)] == w):
                    dp[i] = min(dp[i], dp[i + len(w)])
        return dp[0]

