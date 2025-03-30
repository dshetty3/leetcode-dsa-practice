class Solution(object):
    def numberOfWays(self, s):
        """
        :type s: str
        :rtype: int
        """


        # 0 0 1 1 0 1 1s 3 0s 0
        # 0 1 2 3 4 5
        curr_0 = 3

        res = 0
        curr_1 = 0
        curr_0 = 0
        total_1 = 0
        total_0 = 0

        for c in s:
            if c == '0':
                total_0 += 1
            else:
                total_1 += 1
        
        if s[0] == '0':
            curr_0 += 1
        else:
            curr_1 += 1
        
        for i in range(1, len(s) - 1):
            if s[i] == '0':
                curr_0 += 1
                res += curr_1 * (total_1 - curr_1)
            else:
                curr_1 += 1
                res += curr_0 * (total_0 - curr_0)
        return res
        