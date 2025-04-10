class Solution(object):
    def lastNonEmptyString(self, s):
        """
        :type s: str
        :rtype: str
        """

        count = Counter(s)
        mx = max(count.values())

        res = ""
        seen = set()

        for key, val in count.items():
            if val == mx:
                seen.add(key)

        for c in reversed(s):
            if c in seen and c not in res:
                res += c
        return res[::-1]