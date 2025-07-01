class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """

        n, res = len(word), 1

        for i in range(1, n):
            if word[i - 1] == word[i]:
                res += 1
        return res
        