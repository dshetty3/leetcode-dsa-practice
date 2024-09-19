class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        count = 0
        hamming = x ^ y

        while hamming != 0:
            count += 1
            hamming = hamming & (hamming - 1)
        return count
        