class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """

        orderMap = {c : i for i, c in enumerate(order)}

        for i in range(len(words) - 1):

            word1 = words[i]
            word2 = words[i + 1]

            for j in range(len(word1)):
                if j == len(word2):
                    return False

                if word1[j] != word2[j]:
                    if orderMap[word2[j]] < orderMap[word1[j]]:
                        return False
                    break
        return True
        