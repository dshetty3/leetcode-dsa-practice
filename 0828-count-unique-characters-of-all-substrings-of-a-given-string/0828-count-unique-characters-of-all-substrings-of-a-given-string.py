class Solution(object):
    def uniqueLetterString(self, s):
        """
        :type s: str
        :rtype: int
        """

        cur = res = 0
        last_seen = collections.defaultdict(lambda: [-1, -1])

        for i, char in enumerate(s):
            cur += (i - last_seen[char][0]) - (last_seen[char][0] - last_seen[char][1])
            last_seen[char][1] = last_seen[char][0]
            last_seen[char][0] = i

            res += cur
        
        return res
        