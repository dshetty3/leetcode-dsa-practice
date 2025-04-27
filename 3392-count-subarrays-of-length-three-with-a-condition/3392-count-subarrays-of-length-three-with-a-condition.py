class Solution(object):
    def countSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = 0
        for i in range(1, len(nums) - 1):
            if nums[i] == (nums[i - 1] + nums[i + 1]) * 2:
                res += 1
        return res
        