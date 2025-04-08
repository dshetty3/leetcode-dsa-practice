class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """

        g = defaultdict(list)

        for a, b in connections:
            g[a].append((b, 1))
            g[b].append((a, 0))

        
        q = deque([0])
        visit = set([0])
        change = 0

        while q:
            node = q.popleft()
            for nei, cost in g[node]:
                if nei not in visit:
                    visit.add(nei)
                    change += cost
                    q.append(nei)
        return change

        