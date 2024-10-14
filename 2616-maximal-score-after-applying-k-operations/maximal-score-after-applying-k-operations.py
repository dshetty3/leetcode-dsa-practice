class Solution(object):
    def maxKelements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        maxHeap = [-n for n in nums]
        heapq.heapify(maxHeap)

        while k:
            n = -heapq.heappop(maxHeap) #abs() also works
            res += n
            k -= 1
            heapq.heappush(maxHeap, - int(math.ceil(float(n) / 3)))

        return res 

        