class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        r = 0

        for n in range(1, k + 1):
            r = (r * 10 + 1) % k
            if r == 0:
                return n
        return -1
        