class Solution(object):
    def appealSum(self, s):
        """
        :type s: str
        :rtype: int
        """

        seen = {}
        total = 0

        for i, n in enumerate(s):
            if n in seen:
                left = i - seen[n]
                right = len(s) - i

                total += right * left
            else:
                left = i + 1
                right = len(s) - i

                total += right * left
            
            seen[n] = i
        
        return total
        