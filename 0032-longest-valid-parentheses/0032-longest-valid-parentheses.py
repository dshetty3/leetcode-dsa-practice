class Solution:
    def longestValidParentheses(self, s: str) -> int:


        count = 0

        stack = []

        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')' and stack:
                stack.pop()
                count += 2
            elif len(stack) == 1:
                count = 0
        return count
        