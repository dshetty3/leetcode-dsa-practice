class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        res = []
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i != j and word1 in word2:
                    res.append(word1)
                    break
        return res
        