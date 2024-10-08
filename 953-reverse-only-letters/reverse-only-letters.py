class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """

        l, r = 0, len(s) - 1
        s = list(s)
        while l < r:
            while l < r and not s[l].isalpha():
                l += 1
            while l < r and not s[r].isalpha():
                r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return "".join(s)
        