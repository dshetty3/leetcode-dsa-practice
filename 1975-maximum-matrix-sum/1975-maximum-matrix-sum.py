class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        res = 0
        neg = 0
        mat_min = float('inf')


        for r in matrix:
            for n in r:
                res += abs(n)
                mat_min = min(mat_min, abs(n))
                if n < 0:
                    neg += 1
        if neg & 1:
            res -= 2 * mat_min
        return res
        