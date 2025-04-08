class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """

        stack = []

        for n in num:
            while stack and k > 0 and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)

        
        while stack and k > 0:
            stack.pop()
            k -= 1
        
        res = ''.join(stack).lstrip('0')
        
        return res if res else '0'
        