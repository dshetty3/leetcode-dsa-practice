from collections import defaultdict

class Solution(object):
    def largestPathValue(self, colors, edges):
        """
        :type colors: str
        :type edges: List[List[int]]
        :rtype: int
        """

        adj = defaultdict(list)
        for src, dest in edges:
            adj[src].append(dest)

        n = len(colors)
        count = [[0] * 26 for _ in range(n)]
        visit = set()
        path = set()
        res = 0

        def dfs(node):
            if node in path: 
                return float('inf')
            if node in visit:
                return max(count[node])

            path.add(node)
            colorIdx = ord(colors[node]) - ord('a')

            for nei in adj[node]:
                if dfs(nei) == float('inf'):
                    return float('inf')
                for c in range(26):
                    count[node][c] = max(count[node][c], count[nei][c])

            count[node][colorIdx] += 1
            path.remove(node)
            visit.add(node)

            return max(count[node])

        for i in range(n):
            res = max(res, dfs(i))
            if res == float('inf'):
                return -1

        return res
