class Solution(object):
    def sortMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """

        m = len(grid)
        n = len(grid[0])
        diag = {}

        for i in range(m):
            for j in range(n):
                key = i - j
                if key not in diag: diag[key] = []
                if key < 0: heapq.heappush(diag[key], grid[i][j])
                else: heapq.heappush(diag[key], -grid[i][j])
        
        for i in range(m):
            for j in range(n):
                key = i - j
                if key < 0 : grid[i][j] = heapq.heappop(diag[key])
                else: grid[i][j] = -heapq.heappop(diag[key])
        return grid

        