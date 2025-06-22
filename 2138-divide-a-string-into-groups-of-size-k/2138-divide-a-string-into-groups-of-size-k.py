class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """

        res = []
        for i in range(0, len(s), k):
            c = s[i:i + k]
            if len(c) < k:
                c += fill * (k - len(c))
            res.append(c)
        return res


        