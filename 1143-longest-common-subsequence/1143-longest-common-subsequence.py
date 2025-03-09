class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """

        m = len(text1)
        n = len(text2)

        grid = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    grid[i][j] = grid[i - 1][j - 1] + 1 
                else:
                    grid[i][j] = max(grid[i-1][j], grid[i][j-1])
        return grid[m][n]
            