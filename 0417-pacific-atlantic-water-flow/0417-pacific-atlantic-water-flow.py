class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        p_queue = deque()
        p_seen = set()

        a_queue = deque()
        a_seen = set()

        m = len(heights)
        n = len(heights[0])

        for j in range(n):
            p_queue.append((0,j))
            p_seen.add((0,j))
        
        for i in range(1, m):
            p_queue.append((i,0))
            p_seen.add((i,0))

        for i in range(m):
            a_queue.append((i, n - 1))
            a_seen.add((i, n - 1))
        
        for j in range(n - 1):
            a_queue.append((m - 1,j))
            a_seen.add((m - 1,j))
    
        def getCords(queue, seen):
            coords = set()
            while queue:
                i,j = queue.popleft()
                coords.add((i,j))

                directions = [(1,0),(0,1),(-1,0),(0,-1)]
                for ir, jc in directions:
                    r, c = i + ir, j + jc
                    if 0 <= r < m and 0 <= c < n and heights[r][c] >= heights[i][j] and (r,c) not in seen:
                        seen.add((r,c))
                        queue.append((r,c))
            return coords
        p_coords = getCords(p_queue, p_seen)
        a_coords = getCords(a_queue, a_seen)

        return list(p_coords.intersection(a_coords))

                    


        