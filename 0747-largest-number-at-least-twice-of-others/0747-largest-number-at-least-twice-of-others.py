class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        m = max(nums)

        for x in nums:
            if x != m and m < 2 * x:
                return -1
        return nums.index(m)
        