class Solution(object):
    def platesBetweenCandles(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        left = [-1] * len(s)
        right = [-1] * len(s)
        prefix = [0]

        for i in range(len(s)):
            if s[i] == '|':
                left[i] = i
            else:
                if i > 0:
                    left[i] = left[i - 1]
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '|':
                right[i] = i
            else:
                if i < len(s) - 1:
                    right[i] = right[i + 1]
        
        for i in range(len(s)):
            if s[i] == '*':
                prefix.append(1 + prefix[-1])
            else:
                prefix.append(prefix[-1])
        

        ans = []
        for l, r in queries:
            l = right[l]
            r = left[r]

            if l == -1 or r == -1 or l > r:
                ans.append(0)
            else:
                ans.append(prefix[r + 1] - prefix[l])
        return ans
        