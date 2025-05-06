class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        minHeap = [c for c in count.keys()]
        heapq.heapify(minHeap)

        while minHeap:
            small = minHeap[0]

            for i in range(small, small + k):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True




        