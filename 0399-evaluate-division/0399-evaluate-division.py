class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        adj = defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1 / values[i]])
        

        def bfs(source, target):
            if source not in adj or target not in adj: return -1
            q = deque()
            visit = set()
            q.append([source, 1])
            visit.add(source)

            while q:
                node, w = q.popleft()
                if node == target:
                    return w

                for nei, weight in adj[node]:
                    if nei not in visit:
                        q.append([nei, w * weight])
                        visit.add(nei)
            return -1

        res = []
        for q in queries:
            res.append(bfs(q[0], q[1]))
        return res        

        