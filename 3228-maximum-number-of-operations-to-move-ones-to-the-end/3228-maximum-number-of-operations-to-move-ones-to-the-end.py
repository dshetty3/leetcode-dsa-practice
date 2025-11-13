class Solution(object):
    def maxOperations(self, s):
        """
        :type s: str
        :rtype: int
        """

        count_one = 0
        res = 0
        i = 0
        while i < len(s):
            if s[i] == "0":
                while i + 1 < len(s) and s[i + 1] == "0":
                    i += 1
                res += count_one
            else:
                count_one += 1
            i += 1
        return res
        