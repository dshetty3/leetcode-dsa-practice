class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
        
        if len(q) == 0 or len(q) == n * n:
            return -1
        
        directions = [(-1,0), (0,-1), (1,0), (0,1)]
        distance = -1

        while q:
            distance += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row = dr + r
                    col = dc + c
                    if 0 <= row < n and 0 <= col < n and grid[row][col] == 0:
                        grid[row][col] = 1
                        q.append((row, col))
        return distance
        