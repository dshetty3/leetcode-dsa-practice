class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        nums.sort()

        l = 0
        r = 0
        res = 0
        total = 0

        while r < len(nums):
            total += nums[r]

            while nums[r] * (r - l + 1) > total + k:
                total -= nums[l]
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res
