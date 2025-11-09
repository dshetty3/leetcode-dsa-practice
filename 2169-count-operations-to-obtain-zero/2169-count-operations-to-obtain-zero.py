class Solution(object):
    def countOperations(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """

        res = 0

        while num1 and num2:
            res += num1 // num2
            num1 %= num2
            num1, num2 = num2, num1
        return res
        