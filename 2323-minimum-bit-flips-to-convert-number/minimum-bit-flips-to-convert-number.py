class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """

        res = 0
        n = start ^ goal
        while n:
            res += n & 1
            n = n >> 1
        return res
        