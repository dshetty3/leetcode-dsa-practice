class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        count = Counter(nums)
        heap = []

        for key, val in count.items():
            if len(heap) < k:
                heapq.heappush(heap, (key, val))
            else:
                heapq.heappushpop(heap, (key,val))

        return [h[1] for h in heap]


        