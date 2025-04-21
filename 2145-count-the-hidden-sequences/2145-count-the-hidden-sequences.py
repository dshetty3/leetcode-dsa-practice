class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        """
        :type differences: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        x = y = 0
        curr = 0

        for d in differences:
            curr += d
            x = min(x, curr)
            y = max(y, curr)

            if (y - x) > (upper - lower): return 0
        return (upper - lower) - (y - x) + 1
        