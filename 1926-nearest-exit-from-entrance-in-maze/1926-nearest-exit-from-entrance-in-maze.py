class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """

        ROWS = len(maze)
        COLS = len(maze[0])
        # start = tuple(entrance)
        q = deque([entrance])
        res = 0
        visit = set(entrance)
        directions = [(1,0), (0,1), (-1,0), (0, -1)]

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if [r,c] != entrance and (r == 0 or c == 0 or r == ROWS - 1 or c == COLS - 1): 
                    return res
                for dr,dc in directions:
                    row, col = r + dr, c + dc
                    if 0 <= row < ROWS and 0 <= col < COLS and maze[row][col] == "." and (row,col) not in visit:
                        q.append((row,col))
                        visit.add((row,col))
            res += 1
        return -1
        