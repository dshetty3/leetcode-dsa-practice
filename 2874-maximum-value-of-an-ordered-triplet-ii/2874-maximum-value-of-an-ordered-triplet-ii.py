class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        prefixMax = nums[0]
        max_diff = 0
        res = 0
        for k in range(1, len(nums)):
            res = max(res, max_diff * nums[k])
            prefixMax = max(prefixMax, nums[k])
            max_diff = max(max_diff, prefixMax - nums[k])
            
        return res
        