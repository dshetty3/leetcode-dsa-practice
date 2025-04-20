class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """

        if len(connections) < n - 1:
            return -1
        
        g = defaultdict(list)
        for a, b in connections:
            g[a].append(b)
            g[b].append(a)
        
        visited = set()
        res = 0
        
        def dfs(node):
            visited.add(node)
            for j in g[node]:
                if j not in visited:
                    dfs(j)
        
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        return res - 1
        
        