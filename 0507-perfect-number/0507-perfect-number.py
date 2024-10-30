class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num <= 1:
            return False  

        divisors = []
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                divisors.append(i)  
                if i != 1 and i != num // i:     
                    divisors.append(num // i)

        sum1 = sum(divisors)
        return sum1 == num




        