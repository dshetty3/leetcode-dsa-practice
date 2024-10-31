class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        min_heap = []
        unique = set(nums)

        if len(unique) < 3:
            return max(unique)

        for n in unique:
            heapq.heappush(min_heap, n)

            if len(min_heap) > 3:
                heapq.heappop(min_heap)
        return min_heap[0]


        

        
        