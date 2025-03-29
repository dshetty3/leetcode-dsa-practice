class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """

        ROWS = len(heights)
        COLS = len(heights[0])

        visit = set()
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        minHeap = [[0, 0, 0]] #diff, r, c

        while minHeap:
            diff, r, c = heapq.heappop(minHeap)   

            if (r, c) in visit:
                continue
            visit.add((r,c)) 

            if (r,c) == (ROWS - 1, COLS - 1):
                return diff  

            for dr, dc in direction:
                newR, newC = r + dr, c + dc
                if (newR < 0 or newC < 0 or newC == COLS or newR == ROWS or
                (newR, newC) in visit): continue
                
                newDiff = max(diff, abs(heights[r][c] - heights[newR][newC]))
                heapq.heappush(minHeap, [newDiff ,newR, newC])