class Solution(object):
    def getLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        res = []

        for i in range(len(words)):
            if i == 0 or groups[i] != groups[i - 1]:
                res.append(words[i])
        return res


        