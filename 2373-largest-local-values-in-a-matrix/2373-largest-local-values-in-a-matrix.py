class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """

        N = len(grid)
        res = [[0] * (N - 2) for _ in range (N - 2)]
        for i in range(N - 2):
            for j in range(N - 2):
                res[i][j] = self.find_max(grid, i, j)
        return res
    

    def find_max(self, grid, x, y):
        max_element = 0
        for i in range(x, x + 3):
            for j in range(y, y + 3):
                max_element = max(max_element, grid[i][j])
        return max_element




        