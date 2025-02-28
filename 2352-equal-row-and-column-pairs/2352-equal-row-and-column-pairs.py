class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m = len(grid)
        n = len(grid[0])
        count = 0
        grid2 = []
        for i in range(n):
            column = []
            for j in range(m):
                column.append(grid[j][i])
            grid2.append(column)
        
        for r in grid:
            count += grid2.count(r)
        return count
        
            


        