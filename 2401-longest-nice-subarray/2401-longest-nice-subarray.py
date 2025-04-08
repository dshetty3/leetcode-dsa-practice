class Solution(object):
    def longestNiceSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = 0
        curr = 0
        max_length = 0

        for r in range(len(nums)):
            while curr & nums[r] != 0:
                curr ^= nums[l]
                l += 1
            
            curr |= nums[r]

            max_length = max(max_length, r - l + 1)
        return max_length
        