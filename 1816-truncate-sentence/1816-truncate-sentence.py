class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        words = s.split()

        # for i in range(len(words)):
        #   if i == k:
        #     words.remove(words[i])
        words = words[:k]
        return ' '.join(words)
        