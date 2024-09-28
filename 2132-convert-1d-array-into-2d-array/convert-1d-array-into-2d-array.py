class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """


        # n, n
        # 2n, 2n + n - 1
        # 3n, 3n + n - 1

        if len(original) != m * n:
            return []
        res = []    

        for r in range(m):
            start = r * n
            end = start + n
            res.append(original[start:end])
        return res        