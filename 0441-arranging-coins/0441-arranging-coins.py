class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """

        count = 0

        i = 1
        while n >= 0:
            n -= i
            if n >= 0: 
                count += 1
            i += 1
        return count

        
        