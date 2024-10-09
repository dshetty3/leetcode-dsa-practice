class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """

        openC, closeC = 0, 0

        for c in s:
            if c == '(':
                openC += 1
            elif c == ')':
                if openC > 0:
                    openC -= 1
                else:
                    closeC += 1
        return openC + closeC

        