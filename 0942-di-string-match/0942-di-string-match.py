class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """

        l, h = 0, len(s)
        ans = []
        for x in s:
            if x == 'I':
                ans.append(l)
                l += 1
            else:
                ans.append(h)
                h -= 1
        return ans + [l]
        