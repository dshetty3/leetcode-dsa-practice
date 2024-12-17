class Solution(object):
    def shortestDistanceAfterQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        adj = []
        for i in range(n):
            adj.append([i + 1])
        

        def short_path():
            q = deque()
            q.append((0,0))
            visit = set()
            visit.add((0,0))
            while q:
                cur, length = q.popleft()
                if cur == n - 1:
                    return length
                for nei in adj[cur]:
                    if nei not in visit:
                        q.append((nei, length + 1))
                        visit.add(nei)
        res = []
        for src, dest in queries:
            adj[src].append(dest)
            res.append(short_path())
        return res

        