class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_freq = Counter(s)

        count = 0
        for freq in char_freq.values():
            if freq % 2  == 1:
                count += freq - 1
            else:
                count += freq - 2
        return len(s) - count
        