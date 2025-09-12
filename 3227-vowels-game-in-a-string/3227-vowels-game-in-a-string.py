class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """

        for c in s:
            if c in 'aeiou':
                return True
        return False

        