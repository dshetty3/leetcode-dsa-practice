class Solution(object):
    def maxRemoval(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """

        queries.sort()
        heap = []
        arr = [0] * (len(nums) + 1)
        op = 0
        j = 0

        for i, num in enumerate(nums):
            op += arr[i]
            while j < len(queries) and queries[j][0] == i:
                heapq.heappush(heap, -queries[j][1])
                j += 1
            while op < num and heap and -heap[0] >= i:
                op += 1
                arr[-heapq.heappop(heap) + 1] -= 1
            if op < num:
                return -1
        return len(heap)
        