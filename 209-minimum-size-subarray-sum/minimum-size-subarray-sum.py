class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        sum = 0
        min_length = float('inf')

        for r in range(len(nums)):
            sum += nums[r]
        
            while sum >= target:
                min_length = min(min_length, r - l+ 1)
                sum -= nums[l]
                l += 1
        return min_length if min_length < float('inf') else 0

        