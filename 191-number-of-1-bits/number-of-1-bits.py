class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        # count = 0

        # for i in str(bin(n)):
        #     if i == '1':
        #         count += 1
        # return count

        res = 0

        while n != 0:
            res += 1
            n = n & (n-1)
        return res