class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """

        max_count = 0
        count = 0
        previous = None

        for c in s:
            if c == previous:
                count += 1
            else:
                previous = c
                count = 1
            max_count = max(max_count, count)
        return max_count

        
        