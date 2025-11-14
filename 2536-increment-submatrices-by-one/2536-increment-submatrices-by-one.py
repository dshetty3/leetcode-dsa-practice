class Solution(object):
    def rangeAddQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[List[int]]
        """

        res = [[0] * n for _ in range(n)]

        for t, l, b, r in queries:
            res[t][l] += 1
            if r + 1 < n:
                res[t][r + 1] -= 1
            if b + 1 < n:
                res[b + 1][l] -= 1
            if b + 1 < n and r + 1 < n:
                res[b + 1][r + 1] += 1
        

        for i in range(n):
            for j in range(1, n):
                res[i][j] += res[i][j - 1]
        
        for j in range(n):
            for i in range(1, n):
                res[i][j] += res[i - 1][j]
        
        return res