class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """

        ans = 0

        for i in range(len(s) - 1):
            cur = 0
            for j in range(i + 1):
                if s[j] == '0':
                    cur += 1
            for j in range(i + 1, len(s)):
                if s[j] == '1':
                    cur += 1
            
            ans = max(ans, cur)
        return ans


        