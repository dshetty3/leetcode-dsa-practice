class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """

        # if len(word1) != len(word2): return False

        c1 = Counter(word1)
        c2 = Counter(word2)

        count1 = sorted(c1.values())
        count2 = sorted(c2.values())

        set1 = set(word1)
        set2 = set(word2)

        if count1 == count2 and set1 == set2:
            return True
        
        return False






        