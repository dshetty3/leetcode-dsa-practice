class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        vowelSet = {'a', 'e', 'i', 'o', 'u'}
        l, count, res = 0, 0, 0

        for r in range(len(s)):
            if s[r] in vowelSet:
                count += 1
            if  r - l + 1 > k:
                if s[l] in vowelSet:
                    count -= 1
                l += 1
            res = max(res, count)
        return res
        