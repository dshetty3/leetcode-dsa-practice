class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        # visit = set()
        # queue = deque([(0,0,n - 1)])

        # while queue:
        #     x, y, time = queue.popleft()
        #     if time < 0 or (x,y) in visit:
        #         continue
        #     visit.add((x,y))            

        #     directions = [(0,1),(1,0),(-1,0),(0,-1)]
        #     for dr, dc in directions:
        #         queue.append((x + dr, y + dc, time - 1))
        # return len(visit)

        return 1 + n * (n - 1) * 2








        