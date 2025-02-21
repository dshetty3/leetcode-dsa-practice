class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c):
            if(r < 0 or c < 0 or r == ROWS or c == COLS or 
                not grid[r][c] or (r, c) in visit):
                return 0
            visit.add((r,c))
            res = 1
            direct = [[0, 1], [1, 0], [0, -1], [-1,0]]
            for dr, dc in direct:
                res += dfs(r + dr, c + dc)
            return res

        total = borderLand = 0
        visit = set()
        for r in range(ROWS):
            for c in range(COLS):
                total += grid[r][c]
                if (grid[r][c] and (r,c) not in visit and 
                    (c in [0, COLS - 1] or r in [0, ROWS - 1])):
                    borderLand += dfs(r,c)
        return total - borderLand
        