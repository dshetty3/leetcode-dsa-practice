class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        total = 0

        for i in range(len(nums)):
            min_n = nums[i]
            max_n = nums[i]

            for j in range(i + 1, len(nums)):
                min_n = min(min_n, nums[j])
                max_n = max(max_n, nums[j])
                total += max_n - min_n
        return total

            
        