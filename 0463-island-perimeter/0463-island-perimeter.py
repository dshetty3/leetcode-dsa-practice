class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        perimeter = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1: 
                    perimeter += 4
                    for dr, dc in [(0,1), (1,0), (-1,0), (0,-1)]:
                        row = r + dr
                        col = c + dc 
                        if 0 <= row < m and 0 <= col < n and grid[row][col] == 1:
                            perimeter -= 1
        return perimeter 
        