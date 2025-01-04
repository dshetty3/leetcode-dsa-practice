class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """

        res = 0
        cur = 0

        for c in s:
            if c == '(':
                cur += 1
            elif c == ')':
                cur -= 1
            res = max(res, cur)
        return res
        