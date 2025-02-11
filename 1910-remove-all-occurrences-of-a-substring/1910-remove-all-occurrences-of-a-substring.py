class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """

        stack = []
        for c in s:
            stack.append(c)
        
            if len(stack) >= len(part) and ''.join(stack[-len(part):]) == part:
                for i in range(len(part)):
                    stack.pop()
        return ''.join(stack)
        