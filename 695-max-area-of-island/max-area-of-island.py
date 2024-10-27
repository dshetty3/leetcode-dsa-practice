class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        ROW = len(grid)
        COLS = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= ROW or c < 0 or c >= COLS or grid[r][c] != 1:
                return 0
            else:
                grid[r][c] = 0
                return 1 + (dfs (r + 1, c) +
                            dfs(r - 1, c) +
                            dfs(r, c + 1) +
                            dfs(r, c - 1))
        max_area = 0
        for r in range(ROW):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))

        return max_area
        