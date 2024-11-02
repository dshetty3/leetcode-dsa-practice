class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []

        for c in s:
            if c.isupper():
                res.append(c.lower())
            else:
                res.append(c)
        return ''.join(res)



        