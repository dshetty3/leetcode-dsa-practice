class Solution(object):
    def lengthAfterTransformations(self, s, t):
        """
        :type s: str
        :type t: int
        :rtype: int
        """

        mod = 10 ** 9 + 7
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1
        

        for r in range(t):
            next = [0] * 26
            next[0] = cnt[25]
            next[1] = (cnt[25] + cnt[0]) % mod
            for i in range(2, 26):
                next[i] = cnt[i - 1]
            cnt = next
            
        ans = sum(cnt) % mod
        return ans
        