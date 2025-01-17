class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """

        for i, j in ops:
            m = min(m, i)
            n = min(n, j)
        return m * n

        