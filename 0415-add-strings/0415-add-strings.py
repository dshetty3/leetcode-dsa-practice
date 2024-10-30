class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        carry = 0
        i, j = len(num1) - 1, len(num2) - 1
        res = []

        while i >= 0 or j >= 0 or carry:
            d1 = int(num1[i]) if i >=0 else 0
            d2 = int(num2[j]) if j >= 0 else 0

            total = d1 + d2 + carry
            carry = total // 10
            res.append(total % 10)

            i -= 1
            j -= 1

        res = map(str, res[::-1])
        return "".join(res)

        

        
        
        