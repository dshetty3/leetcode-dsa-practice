class SmallestInfiniteSet(object):

    def __init__(self):
        self.minHeap = []
        self.currMin = 1

        

    def popSmallest(self):
        """
        :rtype: int
        """
        if self.minHeap:
            return heapq.heappop(self.minHeap)
        self.currMin += 1
        return self.currMin - 1
        

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if self.currMin > num and num not in self.minHeap:
            heapq.heappush(self.minHeap, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)