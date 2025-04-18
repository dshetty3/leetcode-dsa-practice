class Solution(object):
    def colorBorder(self, grid, row, col, color):
        """
        :type grid: List[List[int]]
        :type row: int
        :type col: int
        :type color: int
        :rtype: List[List[int]]
        """

        m = len(grid)
        n = len(grid[0])
        visit = set()
        start = grid[row][col]
        borders = []
        directions = [[1,0], [0,1], [-1,0], [0,-1]]



        def is_border(r, c):
            if r in [0, m - 1] or c in [0, n - 1]: return True
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if not (0 <= nr < m or 0 <= nc < n) or grid[nr][nc] != start:
                    return True
            return False 
                
        def dfs(r, c):
            visit.add((r,c))
            if is_border(r,c):
                borders.append((r,c))
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visit and grid[nr][nc] == start:
                    dfs(nr, nc)
        
        dfs(row, col)

        for r, c in borders:
            grid[r][c] = color
        return grid
            

        

            
        