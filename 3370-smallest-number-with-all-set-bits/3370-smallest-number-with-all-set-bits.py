class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        x = 1
        while x < n:
            x = x * 2 + 1
        return x
        