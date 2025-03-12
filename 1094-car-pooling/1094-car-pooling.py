class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        trips.sort(key = lambda t:t[1])
        currSum = 0
        minHeap = [] # [end, passengers]

        for t in trips:
            numPassengers, start, end = t
            while minHeap and minHeap[0][0] <= start:
                currSum -= minHeap[0][1]
                heapq.heappop(minHeap)
            
            currSum += numPassengers
            if currSum > capacity:
                return False
            heapq.heappush(minHeap,[end, numPassengers])
        return True

