class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 1, x
        res = 0

        while l <= r:
            mid = (l + (r-l)//2)
            if mid**2 > x:
                r = mid - 1
            elif mid**2 < x:
                l = mid + 1
            else:
                return mid
        return r
        