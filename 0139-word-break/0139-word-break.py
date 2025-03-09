class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        # wordSet = set(wordDict)

        # def dfs(i):
        #     if i == len(s):
        #         return True
            
        #     for j in range(i, len(s)):
        #         if s[i: j + 1] in wordSet:
        #             if dfs(j + 1):
        #                 return True
        #     return False
        # return dfs(0)


        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w) <= len(s) and s[i: i+ len(w)] == w):
                    dp[i] = dp[i + len(w)]
                if dp[i]: break
        return dp[0]
