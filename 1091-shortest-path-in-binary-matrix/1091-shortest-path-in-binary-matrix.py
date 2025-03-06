class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        N = len(grid)
        if grid[0][0] == 1 or grid[N - 1][N - 1] == 1:
            return -1
        direct = [[1,0], [-1,0], [0,1], [0,-1], [1,1],[-1,-1], [-1,1], [1,-1]]
        q = deque()
        q.append((0,0,1))
        grid[0][0] = 1
        while q:
            r, c, length = q.popleft()
            if r == N -1 and c == N - 1:
                return length

            for dr, dc in direct:
                nr, nc = r + dr, c + dc
                if min(nr, nc) >= 0 and max(nr, nc) < N and grid[nr][nc] == 0:
                    q.append((nr, nc, length + 1))
                    grid[nr][nc] = 1

        return -1

        