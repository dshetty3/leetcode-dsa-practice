class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        longest = 0
        l = 0
        count = [0] * 26

        for r in range(len(s)):
            count[ord(s[r]) - 65] += 1
            while (r-l+1) - max(count) > k:
                count[ord(s[l]) - 65] -= 1
                l += 1

            longest = max(r-l+1, longest)
        return longest
        