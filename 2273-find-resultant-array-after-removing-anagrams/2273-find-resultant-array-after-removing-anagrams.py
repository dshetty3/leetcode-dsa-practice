class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        n = len(words)
        freq = [Counter(w) for w in words]
        res = [words[0]]
        for i in range(1, n):
            if freq[i] != freq[i - 1]:
                res.append(words[i])
        return res
        