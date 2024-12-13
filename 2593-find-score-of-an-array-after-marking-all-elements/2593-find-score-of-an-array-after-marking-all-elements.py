class Solution(object):
    def findScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans = 0
        marked = [False] * len(nums)

        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i], i))
        
        while heap:
            num, index = heapq.heappop(heap)
            if not marked[index]:
                ans += num
                marked[index] = True
                if index - 1 >= 0:
                    marked[index - 1] = True
                if index + 1 < len(nums):
                     marked[index + 1] = True 
        return ans   

        