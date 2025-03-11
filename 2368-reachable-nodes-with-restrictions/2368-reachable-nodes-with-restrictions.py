class Solution(object):
    def reachableNodes(self, n, edges, restricted):
        """
        :type n: int
        :type edges: List[List[int]]
        :type restricted: List[int]
        :rtype: int
        """


        adj = defaultdict(list)
        total = 1
        visited = set(restricted)
        visited.add(0)
        q = deque([0])
        

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        

        while len(q):
            node = q.popleft()
            for nei in adj[node]:
                if nei not in visited:
                    q.append(nei)
                    total += 1  
                    visited.add(nei)
        return total
        
        