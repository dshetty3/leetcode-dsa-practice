class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        N = len(grid)
        directions = [[0, -1], [-1, 0], [1, 0], [0,1]]
        visit = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r == N or c == N or grid[r][c] != 1 or (r, c) in visit:
                return
            visit.add((r,c))
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                dfs(row, col)
        
        def bfs():
            q = deque(visit)
            res = 0

            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in directions:
                        row = dr + r
                        col = dc + c
                        if row < 0 or col < 0 or row == N or col == N or (row, col) in visit:
                            continue
                        if grid[row][col] == 1:
                            return res
                        visit.add((row, col))
                        q.append([row, col])
                res += 1

        

        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    dfs(r,c)
                    return bfs()
        