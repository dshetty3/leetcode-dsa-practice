class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """

        ans = 0
        nums = [start + 2 * n for n in range(n)]

        for n in nums:
            ans = ans ^ n
        return ans


        