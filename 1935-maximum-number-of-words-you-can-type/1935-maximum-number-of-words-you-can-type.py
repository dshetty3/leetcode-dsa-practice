class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        words = text.split()
        count = 0

        for w in words:
            for c in brokenLetters:
                if c in w:
                    count += 1
                    break
        return len(words) - count        