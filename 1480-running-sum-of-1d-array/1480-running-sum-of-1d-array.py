class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        total = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            total[i + 1] = total[i] + nums[i]
        return total[1:]


