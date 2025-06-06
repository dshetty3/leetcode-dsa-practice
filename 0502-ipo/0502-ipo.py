class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """

        maxProfit = []
        minCap = [(c,p) for c,p in zip(capital, profits)]

        for i in range(k):

            while minCap and minCap[0][0] <= w:
                c, p = heapq.heappop(minCap)
                heapq.heappush(maxProfit, -1 * p)
            if not maxProfit: break
            w += -1 * heapq.heappop(maxProfit)
        return w
        