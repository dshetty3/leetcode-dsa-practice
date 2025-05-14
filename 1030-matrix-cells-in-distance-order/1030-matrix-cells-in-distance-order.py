class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        
        def dfs(r, c):
            visit.add((r, c))
            res.append([r, c])
            for dr, dc in (r - 1, c), (r + 1, c), (r, c + 1), (r, c - 1):
                if 0 <= dr < rows and 0 <= dc < cols and (dr, dc) not in visit:
                    dfs(dr, dc)


        res = []
        visit = set()
        dfs(rCenter, cCenter)
        return sorted(res, key = lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))