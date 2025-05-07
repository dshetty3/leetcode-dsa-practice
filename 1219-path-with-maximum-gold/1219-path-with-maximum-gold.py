class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c, visit):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == 0 or(r, c) in visit):
                return 0
            visit.add((r,c))
            res = grid[r][c]
            directions = [(r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1)]
            for nr, nc in directions:
                res = max(res, grid[r][c] + dfs(nr, nc, visit))
            visit.remove((r,c))
            return res

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c, set()))
        return res
        