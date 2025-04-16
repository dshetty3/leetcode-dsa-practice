class Solution:
    def reverseParentheses(self, s: str) -> str:

        stack = []

        for c in s:
            if c == ')':
                section = []
                while stack[-1] != '(':
                    section.append(stack.pop())
                stack.pop()
                stack.extend(section)
            else:
                stack.append(c)
        return "".join(stack)
        