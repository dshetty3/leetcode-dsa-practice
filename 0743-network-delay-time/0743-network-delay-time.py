class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """

        graph = defaultdict(list)
        for u, v, time in times:
            graph[u].append((v, time))
        
        min_times = {}
        min_heap = [(0, k)]

        while min_heap:
            dist, node = heapq.heappop(min_heap)
            if node in min_times:
                continue
            
            min_times[node] = dist
            for nei, nei_time in graph[node]:
                if nei not in min_times:
                    heapq.heappush(min_heap, (dist + nei_time, nei))
                
        if len(min_times) == n:
            return max(min_times.values())
        else:
            return -1
        

        