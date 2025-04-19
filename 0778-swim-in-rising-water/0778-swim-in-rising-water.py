class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        N = len(grid)
        visit = set()
        minHeap = [(grid[0][0], 0, 0)] #height, row, col
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        visit.add((0,0))

        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            visit.add((r,c))

            if r == N - 1 and c == N -1:
                return t
            for dr, dc in directions:
                row = dr + r
                col = dc + c
                if (row < 0 or col < 0 or row == N or col == N or (row,col) in visit):
                    continue
                visit.add((row,col))
                heapq.heappush(minHeap, (max(t, grid[row][col]), row, col))

        