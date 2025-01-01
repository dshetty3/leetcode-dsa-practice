class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res = []

        s = sorted(nums)

        for n in nums:
            res.append(s.index(n))
        return res
        