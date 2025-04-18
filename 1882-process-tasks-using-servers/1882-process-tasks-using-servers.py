import heapq

class Solution(object):
    def assignTasks(self, servers, tasks):
        """
        :type servers: List[int]
        :type tasks: List[int]
        :rtype: List[int]
        """
        res = [0] * len(tasks)

        # Min-heap of available servers: (weight, index)
        available = [(servers[i], i) for i in range(len(servers))]
        heapq.heapify(available)

        # Min-heap of unavailable servers: (available_time, weight, index)
        unavailable = []

        time = 0

        for i in range(len(tasks)):
            time = max(time, i)

            # If no server is available, move time forward to the next available server
            if not available:
                time = unavailable[0][0]

            # Move servers that have become available to the available heap
            while unavailable and time >= unavailable[0][0]:
                available_time, weight, index = heapq.heappop(unavailable)
                heapq.heappush(available, (weight, index))

            # Assign task to the best available server
            weight, index = heapq.heappop(available)
            res[i] = index
            heapq.heappush(unavailable, (time + tasks[i], weight, index))

        return res
