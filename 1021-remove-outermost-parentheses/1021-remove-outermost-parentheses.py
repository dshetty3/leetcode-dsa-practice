class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """

        ans = ""
        count = 0

        for c in s:
            if count == 0 and c == '(':
                count += 1 
            elif c == '(':
                count += 1
                ans += c
            elif count == 1 and c == ')':
                count -= 1
            else:
                count -= 1
                ans += c
        return ans        