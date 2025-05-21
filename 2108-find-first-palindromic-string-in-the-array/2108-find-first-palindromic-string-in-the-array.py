class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        for w in words:
            l = 0
            r = len(w) - 1
            while w[l] == w[r]:
                if l >= r:
                    return w
                l += 1
                r -= 1

        return ""

        