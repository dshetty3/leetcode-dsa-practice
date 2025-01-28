class Solution(object):
    def findMaxFish(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def dfs(r,c):
            if (r < 0 or c < 0 
            or r == ROWS or c == COLS
            or grid[r][c] == 0 or (r,c) in visit):
                return 0
            visit.add((r,c))
            res = grid[r][c]

            neighbours = [[r+1, c], [r, c+1], [r, c-1], [r-1,c]]
            for nr, nc in neighbours:
                res += dfs(nr, nc)
            return res

        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0
        visit = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] and (r,c) not in visit:
                    res = max(res, dfs(r,c))

        return res
        