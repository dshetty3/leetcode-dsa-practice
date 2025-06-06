class Solution(object):
    def robotWithString(self, s):
        """
        :type s: str
        :rtype: str
        """

        count = Counter(s)
        stack = []
        res = []
        minChar = 'a'

        for c in s:
            stack.append(c)
            count[c] -= 1
            while minChar != 'z' and count[minChar] == 0:
                minChar = chr(ord(minChar) + 1)
            while stack and stack[-1] <= minChar:
                res.append(stack.pop())
        return ''.join(res)
        