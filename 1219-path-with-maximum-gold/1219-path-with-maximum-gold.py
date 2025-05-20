class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        res = 0


        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visit or grid[r][c] == 0):
                return 0
            visit.add((r, c))
            res = grid[r][c]
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                res = max(res, grid[r][c] + dfs(row, col))
            visit.remove((r, c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c))
        return res
                
            
                    

        