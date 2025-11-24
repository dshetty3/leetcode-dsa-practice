class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """

        res = list()
        prefix = 0
        for n in nums:
            prefix = ((prefix << 1) + n) % 5
            res.append(prefix == 0)
        return res
        