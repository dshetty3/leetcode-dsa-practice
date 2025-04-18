class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        for i, t in enumerate(tasks):
            t.append(i)
        
        tasks.sort(key = lambda t:t[0])

        res = []
        minHeap = []
        i = 0
        time = tasks[0][0]


        while minHeap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minHeap, (tasks[i][1], tasks[i][2]))
                i += 1
            

            if not minHeap:
                time = tasks[i][0]
            else:
                processTime, idx = heapq.heappop(minHeap)
                time += processTime
                res.append(idx)
        return res
        