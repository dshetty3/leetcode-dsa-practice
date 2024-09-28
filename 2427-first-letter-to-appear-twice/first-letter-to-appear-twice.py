class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """

        duplicates = []

        for c in s:
            if c in duplicates:
                return c
            
            duplicates.append(c)
        