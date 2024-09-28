class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        res = []

        for word in words:
            for row in rows:
                # if all (c in row for c in word.lower()):
                #     res.append(word)
                #     break
                if set(word.lower()).issubset(row):
                    res.append(word)
                    break
        return res

        