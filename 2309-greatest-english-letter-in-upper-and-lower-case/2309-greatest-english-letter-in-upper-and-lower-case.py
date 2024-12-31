class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""


        for c in s:
            if c.isupper() and c.lower() in s:
                if c > res:
                    res = c.upper()

        return res
        