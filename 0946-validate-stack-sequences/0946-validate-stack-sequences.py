class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        i = 0
        stack = []

        for n in pushed:
            stack.append(n)
            while stack and i < len(popped) and popped[i] == stack[-1]:
                stack.pop()
                i += 1
        return not stack

        