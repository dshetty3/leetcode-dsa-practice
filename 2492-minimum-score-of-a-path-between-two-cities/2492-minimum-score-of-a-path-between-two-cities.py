class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = collections.defaultdict(list)

        for src, dest, dist in roads:
            adj[src].append((dest, dist))
            adj[dest].append((src, dist))
        
        def dfs(i):
            if i in visit: return
            visit.add(i)
            nonlocal res

            for nei, dist in adj[i]:
                res = min(res, dist)
                dfs(nei)
        
        res = float("inf")
        visit = set()
        dfs(1)
        return res
        