class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        vowel_set = set('aeiou')

        prefix_count = [0] * (len(words) + 1)
        prev = 0
        for i, w in enumerate(words):
            if w[0] in vowel_set and w[-1] in vowel_set:
                prev += 1
            prefix_count[i + 1] = prev
        

        res = [0] * len(queries)
        for i, q in enumerate(queries):
            l, r = q
            res[i] = prefix_count[r + 1] - prefix_count[l]
        return res

        