class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        posCount = len(nums) - self.upper(nums)
        negCount = self.lower(nums)

        return max(posCount, negCount)

    def lower(self, nums):
        l = 0
        r = len(nums) - 1
        idx = len(nums)

        while l <= r:
            m = (l + r) // 2
            if nums[m] < 0:
                l = m + 1
            else:
                r = m - 1
                idx = m
        return idx

    def upper(self, nums):
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] <= 0:
                l = m + 1
            else:
                r = m - 1
                idx = m
        return idx