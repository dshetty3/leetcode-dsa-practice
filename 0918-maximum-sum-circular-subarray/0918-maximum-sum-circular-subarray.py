class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        currMin, currMax = 0, 0
        globalMin, globalMax = nums[0], nums[0]
        total = 0


        for n in nums:
            currMax = max(currMax + n, n)
            currMin = min(currMin + n, n)
            total += n
            globalMax = max(globalMax, currMax)
            globalMin =min(globalMin, currMin)
        
        return max(globalMax, total - globalMin) if globalMax > 0 else globalMax
        