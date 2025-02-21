class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """

        curSet = set()
        res = 1

        for c in s:
            if c in curSet:
                res += 1
                curSet = set()
            curSet.add(c)
        return res

        