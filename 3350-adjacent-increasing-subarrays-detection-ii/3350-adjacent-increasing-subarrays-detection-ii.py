class Solution(object):
    def maxIncreasingSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

      
        count = 1
        res = 0
        percent = 0
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                count += 1
            else:
                percent = count
                count = 1
            res = max(res, min(percent, count))
            res = max(res, count // 2)
        return res
        