class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        dp[-1][-1] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                
                match = i < len(s) and (s[i] == p[j] or p[j] == '.')
                if j + 1 < len(p) and p[j + 1] == '*':
                    dp[i][j] = dp[i][j + 2] or match and dp[i + 1][j]
                else:
                    dp[i][j] = match and dp[i + 1][j + 1]
        return dp[0][0]


        # def dfs(i, j):
        #     if i >= len(s) and j >= len(p): return True
        #     if j >= len(p): return False


        #     match = i < len(s) and (s[i] == p[j] or p[j] == '.')
        #     if (j + 1) < len(p) and p[j + 1] == '*':
        #         return (dfs(i, j + 2) or (match and dfs(i + 1, j)))

        #     if match:
        #         return dfs(i + 1, j + 1)
            
        #     return False
        
        # return dfs(0, 0)

        