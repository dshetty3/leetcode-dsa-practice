class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """

        count = Counter(s)
        maxOdd = 0
        minEven = float('inf')

        for c in count.values():
            if c % 2 == 1:
                maxOdd = max(maxOdd, c)
        
        for c in count.values():
            if c % 2 == 0:
                minEven = min(minEven, c)
        
        return maxOdd - minEven

        