class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        words = s.split()
        for word in words:
            c = words[::-1]
        return ' '.join(c)

        