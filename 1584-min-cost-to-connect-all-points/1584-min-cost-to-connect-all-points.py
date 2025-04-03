class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        total_cost = 0
        seen = set()
        min_heap = [(0, 0)]

        while len(seen) < len(points): #
            distance, i = heapq.heappop(min_heap)
            if i in seen:
                continue
            seen.add(i)
            total_cost += distance
            xi, yi = points[i]

            for j in range(len(points)):
                if j not in seen:
                    xj, yj = points[j]
                    nei_distance = abs(xi - xj) + abs(yi - yj)
                    heapq.heappush(min_heap, (nei_distance, j))
            
        return total_cost


        