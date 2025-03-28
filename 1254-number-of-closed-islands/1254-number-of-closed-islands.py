class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        ROWS , COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS):
                return 0
            if grid[r][c] == 1 or (r, c) in visit:
                return 1

            visit.add((r,c))
            return min (dfs(r, c + 1),
                        dfs(r, c - 1),
                        dfs(r + 1, c),
                        dfs(r - 1, c))

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if not grid[r][c] and (r,c) not in visit:
                    res += dfs(r, c)
        return res


        