class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """

        # heights = [0] * len(mat[0])
        # ans = 0
        # for r in mat:
        #     for i, x in enumerate(r):
        #         heights[i] = 0 if x == 0 else heights[i] + 1
        #     stack = [[-1, 0, -1]]
        #     for i, h in enumerate(heights):
        #         while stack[-1][2] >= h:
        #             stack.pop()
        #         j, prev, _ = stack[-1]
        #         cur = prev + (i - j) + h
        #         stack.append([i, cur, h])
        #         ans += cur
        # return ans

        ROWS = len(mat)
        COLS = len(mat[0])
        res = 0
        row = [[0] * COLS for _ in range(ROWS)]

        for i in range(ROWS):
            for j in range(COLS):
                if j == 0:
                    row[i][j] = mat[i][j]
                else:
                    row[i][j] = 0 if mat[i][j] == 0 else row[i][j-1] + 1
                cur = row[i][j]
                for k in range(i, -1, -1):
                    cur = min(cur, row[k][j])
                    if cur == 0: break
                    res += cur
        return res
