class Solution(object):
    def minTimeToReach(self, moveTime):
        """
        :type moveTime: List[List[int]]
        :rtype: int
        """

        ROWS = len(moveTime)
        COLS = len(moveTime[0])

        visited = [[False] * COLS for _ in range(ROWS)]

        visit = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = [(0, 0, 0)]
        heapq.heapify(q)
        curr_time = 0

        while q:
            curr_time, r, c = heapq.heappop(q)
            if r == ROWS - 1 and c == COLS - 1:
                return curr_time
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                if 0 <= row < ROWS and 0 <= col < COLS and(row, col) not in visit:
                    visited[row][col] = True

                    if curr_time >= moveTime[row][col]:
                        heapq.heappush(q, (curr_time + 1, row, col))
                    else:
                        heapq.heappush(q, (moveTime[row][col] + 1, row, col))
                    visit.add((row, col))
        return -1
                        