class Solution(object):
    def maxMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        memo = {}

        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r,c)]
        
            max_move = 0
            directions = [(0, 1), (-1, 1), (1, 1)]

            for dr, dc in directions:
                new_row, new_col = dr + r, dc + c
                if 0 <= new_row < m and new_col < n and grid[new_row][new_col] > grid[r][c]:
                    max_move = max(max_move, 1 + dfs(new_row, new_col))
            memo[(r, c)] = max_move
            return max_move

        max_path = 0

        for i in range(m):
            max_path = max(max_path, dfs(i, 0))
        return max_path

            


        
        