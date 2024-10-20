class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                #substring pop
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()
                #check integer

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                stack.append(int(k) * substr)

        return "".join(stack)
        