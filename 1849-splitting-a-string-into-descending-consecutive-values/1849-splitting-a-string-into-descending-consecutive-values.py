class Solution(object):
    def splitString(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def backtrack(i, prev):
            if i == len(s):
                return True

            for j in range(i, len(s)):
                newPrev = int(s[i: j + 1])
                if newPrev + 1 == prev and backtrack(j + 1, newPrev):
                    return True
            return False

        for i in range(len(s) - 1):
            val = int(s[:i + 1]) 
            if backtrack(i + 1, val):
                return True
        return False    