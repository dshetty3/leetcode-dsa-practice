class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """

        closeB = 0
        Max = 0

        for c in s:
            if c == '[':
                closeB -= 1
            else:
                closeB += 1
            Max = max(Max,closeB)
        return (Max + 1) // 2

        
        return 
        