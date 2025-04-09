class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        stack = [-1]

        count = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif len(stack) == 1:
                stack[0] = i
            else:
                stack.pop()
                count = max(count, i - stack[-1])
        return count
        