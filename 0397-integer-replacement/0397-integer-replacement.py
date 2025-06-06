class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """


        count = 0

        while n != 1:
            if n % 2 == 0:
                n = n // 2
            elif n % 4 == 1 or n == 3:
                n -= 1
            else:
                n = n + 1
            count += 1
        return count
        