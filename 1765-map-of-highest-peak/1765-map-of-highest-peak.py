class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:

        ROWS = len(isWater)
        COLS = len(isWater[0])

        q = deque()
        visit = set()
        res = [[-1] * COLS for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                if isWater[r][c] == 1:
                    q.append((r,c))
                    visit.add((r,c))
                    res[r][c] = 0

        while q:
            r, c = q.popleft()
            h = res[r][c]

            neighbours = [[r+1, c], [r, c+1], [r-1,c], [r,c-1]]
            for nr, nc in neighbours:
                if (nr < 0 or nc < 0 or
                    nr == ROWS or nc == COLS or
                    (nr, nc) in visit):
                        continue
                q.append((nr,nc))
                visit.add((nr,nc))
                res[nr][nc] = h + 1
        return res


            