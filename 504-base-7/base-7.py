class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """

        if num == 0:
            return '0'

        sign = '-' if num < 0 else ''
        remainders = []
        n = abs(num)

        while n > 0:
            
            remainder = n % 7
            remainders.append(str(remainder))
            n //= 7
        
        remainders.reverse()
        return sign + ''.join(remainders) 







        