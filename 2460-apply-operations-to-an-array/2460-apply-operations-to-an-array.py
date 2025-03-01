class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                nums[i - 1] *= 2
                nums[i] = 0

        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
            r += 1
        return nums
