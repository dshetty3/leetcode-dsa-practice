class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s_list = list(s)
        for i in range(1, len(s) - 1):
            for j in range(len(s) - i):
                digit1 = ord(s_list[j]) - ord("0")
                digit2 = ord(s_list[j + 1]) - ord("0")
                s_list[j] = chr(((digit1 + digit2) % 10) + ord("0"))
        return s_list[0] == s_list[1]
        