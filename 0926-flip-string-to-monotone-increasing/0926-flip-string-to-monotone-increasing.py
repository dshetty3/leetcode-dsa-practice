class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """

        res = 0
        countOne = 0
        for c in s:
            if c == '1':
                countOne += 1
            else:
                res = min(1 + res, countOne)
        return res

        