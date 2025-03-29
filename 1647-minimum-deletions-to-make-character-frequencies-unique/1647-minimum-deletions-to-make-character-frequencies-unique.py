class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """

        count = {}
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1

        used_freq = set()
        res = 0

        for c, freq in count.items():
            while freq > 0 and freq in used_freq:
                freq -= 1
                res += 1
            used_freq.add(freq)
        return res


        