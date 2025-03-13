class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        incoming = defaultdict(list)

        for src, dest in edges:
            incoming[dest].append(src)
        
        res = []
        for i in range(n):
            if not incoming[i]:
                res.append(i)
        return res
        