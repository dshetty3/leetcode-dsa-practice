class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """

        if n % 2 != 0:
            return 'x' * n
        return ('x' * (n - 1)) + 'y'

        
        