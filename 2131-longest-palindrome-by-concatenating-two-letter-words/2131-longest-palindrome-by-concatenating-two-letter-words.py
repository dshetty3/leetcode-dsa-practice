class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        length = 0
        count = Counter()

        for w in words:
            rev = w[1] + w[0]
            if count[rev] > 0:
                length += 4
                count[rev] -= 1
            else:
                count[w] += 1
        
        for word, count in count.items():
            if count > 0 and word[0] == word[1]:
                return length + 2
        return length
        