class Solution(object):
    def findChampion(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        incoming = [0] * n

        for s, d in edges:
            incoming[d] += 1
        
        champions = []

        for i, incoming_cnt in enumerate(incoming):
            if not incoming_cnt:
                champions.append(i)
        
        if len(champions) > 1:
            return -1
        
        return champions[0]
        


        