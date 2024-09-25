class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        temp = num
        bit = 1

        while temp:
            num = num ^ bit
            bit = bit << 1
            temp = temp >> 1
        return num
