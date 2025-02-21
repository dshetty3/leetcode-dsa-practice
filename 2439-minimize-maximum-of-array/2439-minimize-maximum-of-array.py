class Solution(object):
    def minimizeArrayValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = total = nums[0]

        for i in range(1, len(nums)):
            total += nums[i]
            res = max(res, (total + i) // (i + 1))
        return res
        