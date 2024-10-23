class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = s.lstrip()
        sign = 1

        if s.startswith('-'):
            sign = -1
            s = s[1:]
        elif s.startswith('+'):
            s = s[1:]
        

        curr = 0

        for i in range(len(s)):
            if not s[i].isdigit():
                break
            curr = curr * 10 + int(s[i])

        curr = curr * sign

        curr = min(curr, 2 ** 31 - 1)
        curr = max(curr, -(2 ** 31))

        return curr
        