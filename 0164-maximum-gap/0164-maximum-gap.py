class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        nums.sort()

        max_gap = 0
        curr_gap = 0

        if len(nums) == 1: return 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] >= curr_gap:
                curr_gap = nums[i] - nums[i - 1]
            max_gap = max(max_gap, curr_gap)
        return max_gap

        