class Solution(object):
    def maxDistinctElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        nums.sort()

        count = 0
        prev = float('-inf')

        for n in nums:
            curr = min(max(n - k, prev + 1), n + k)
            if curr > prev:
                count += 1
                prev = curr
        return count
        