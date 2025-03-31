class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """

        zeros = 0
        ones = 0
        for c in s:
            if c == '0':
                zeros += 1
            else:
                ones += 1
        
        if abs(zeros - ones) > 1:
            return -1
        
        if zeros > ones:
            return self.swap(s, '0')
        elif ones > zeros:
            return self.swap(s, '1')
        else:
            return min(self.swap(s, '0'), self.swap(s, '1'))
        
    def swap(self, s, c):
        swaps = 0

        for c1 in s:
            if c1 != c:
                swaps += 1
            
            c = '1' if c == '0' else '0'
        return swaps // 2
        