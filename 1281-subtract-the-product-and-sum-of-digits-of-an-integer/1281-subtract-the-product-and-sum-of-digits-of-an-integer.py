class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum1 = 0
        product = 1

        while n > 0:
            digit = n % 10
            sum1 += digit
            product *= digit
            n //= 10
        # print(sum1)
        # print(product)
        return product - sum1
        