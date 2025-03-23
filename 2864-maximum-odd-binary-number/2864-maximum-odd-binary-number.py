class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = 0
        for i in range(len(s)):
            if s[i] == '1':
                count += 1
        
        return '1' * (count - 1) + '0' * (len(s) - count)  + '1'
        