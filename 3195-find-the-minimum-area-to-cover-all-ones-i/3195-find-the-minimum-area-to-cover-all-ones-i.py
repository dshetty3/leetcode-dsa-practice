class Solution(object):
    def minimumArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        ROWS = len(grid)
        COLS = len(grid[0])

        min_i, min_j = COLS, ROWS
        max_i, max_j = 0, 0


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    min_i = min(min_i, i)
                    max_i = max(max_i, i)
                    min_j = min(min_j, j)
                    max_j = max(max_j, j)
        return (max_i - min_i + 1) * (max_j - min_j + 1)



        