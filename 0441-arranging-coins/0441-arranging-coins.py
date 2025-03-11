class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """

        # count = 0

        # i = 1
        # while n >= 0:
        #     n -= i
        #     if n >= 0: 
        #         count += 1
        #     i += 1
        # return count


        l = 1
        r = n
        res = 0

        while l <= r:
            m = (l + r) // 2
            coins = (m / 2) * (m + 1)
            if coins > n:
                r = m - 1
            else:
                l = m + 1
                res = max(res, m)
        return res
        
        