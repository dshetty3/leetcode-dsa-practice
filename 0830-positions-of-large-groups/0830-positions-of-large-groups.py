class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """

        res = []
        i = 0

        while i < len(s):
            j = i
            while j < len(s) and s[i] == s[j]:
                j += 1
            if j - i >= 3:
                res.append([i, j - 1])
            i = j
        return res

        
        