class Solution(object):
    def closestMeetingNode(self, edges, node1, node2):
        """
        :type edges: List[int]
        :type node1: int
        :type node2: int
        :rtype: int
        """

        adj = defaultdict(list)
        for i, dist in enumerate(edges):
            adj[i].append(dist)

        def bfs(src, distMap):
            q = deque()
            q.append([src, 0])
            distMap[src] = 0

            while q:
                node, dist = q.popleft()
                for nei in adj[node]:
                    if nei not in distMap:
                        q.append([nei, dist + 1])
                        distMap[nei] = dist + 1
        

        node1Dist = {}
        node2Dist = {}
        bfs(node1, node1Dist)
        bfs(node2, node2Dist)

        res = -1
        resDist = float('inf')
        for i in range(len(edges)):
            if i in node1Dist and i in node2Dist:
                dist = max(node1Dist[i],node2Dist[i])
                if dist < resDist:
                    res = i
                    resDist = dist
        return res

