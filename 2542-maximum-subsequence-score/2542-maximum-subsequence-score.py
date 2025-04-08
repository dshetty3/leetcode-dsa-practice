class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """

        pairs = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
        pairs = sorted(pairs, key=lambda x:x[1], reverse =True)
        minHeap = []
        res = 0
        n1Sum = 0

        for n1, n2 in pairs:
            n1Sum += n1
            heapq.heappush(minHeap, n1)
            if len(minHeap) == k:
                res = max(res, n1Sum * n2)
            if len(minHeap) > k:
                n1Sum -=  heapq.heappop(minHeap)
        return res


        