class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        dp= defaultdict(int)


        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c]:
                    dp[(r,c)] = 1 + min(
                        dp[(r - 1, c)],
                        dp[(r, c - 1)],
                        dp[(r - 1, c - 1)]
                    )

                    res += dp[(r, c)]
        return res
        