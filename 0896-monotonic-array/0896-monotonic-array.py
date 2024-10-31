class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        increment = True
        decrement = True

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                increment = False
            if nums[i] > nums[i -1]:
                decrement = False
        return increment or decrement 
        