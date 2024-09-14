class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """

        count = 0

        for n in range(len(s)):
            if (n == 0 or s[n - 1] == " ") and s[n] != " ":
                count += 1
        return count



        