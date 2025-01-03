class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        left = 0
        right = sum(nums)

        for i in range(len(nums) - 1):
            left += nums[i]
            right -= nums[i]
            if left >= right:
                count += 1
        return count
        