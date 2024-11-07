class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_count = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1
        return max_count


        
        