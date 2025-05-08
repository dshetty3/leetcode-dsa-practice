class Solution(object):
    def minTimeToReach(self, moveTime):
        """
        :type moveTime: List[List[int]]
        :rtype: int
        """

        ROWS = len(moveTime)
        COLS = len(moveTime[0])
        heap = [(0, 0, 0)]
        visited = [[float('inf') for i in range(COLS)] for j in range(ROWS)]
        directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        visited[0][0] = 0

        while heap:
            time, r, c = heapq.heappop(heap)

            if visited[r][c] < time:
                continue
            
            visited[r][c] = time

            for dr, dc in directions:
                row = dr + r
                col = dc + c

                if row < 0 or row == ROWS or col < 0 or col == COLS:
                    continue
                
                next = max(visited[r][c], 
                                moveTime[row][col]) + (r + c) % 2 + 1

                if next < visited[row][col]:
                    visited[row][col] = next
                    heapq.heappush(heap, (next, row, col))
        return visited[ROWS - 1][COLS - 1]




        