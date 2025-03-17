class MedianFinder(object):

    def __init__(self):
        self.small = [] #maxheap
        self.large = [] #minheap
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.small, -1 * num)

        if (self.small and self.large and abs(self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)


    def findMedian(self):
        """
        :rtype: float
        """

        if len(self.small) > len(self.large): #odd
            return -1 * self.small[0]
        elif len(self.small) < len(self.large): #even
            return self.large[0]
        
        return (-1 * self.small[0] + self.large[0]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()