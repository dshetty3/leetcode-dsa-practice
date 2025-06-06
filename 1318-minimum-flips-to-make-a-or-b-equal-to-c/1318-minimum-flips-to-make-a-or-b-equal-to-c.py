class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        res = 0
        while a > 0 or b > 0 or c > 0:
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1

            if bit_c == 0:
                res += (bit_a + bit_b)
            else:
                if bit_a == 0 and bit_b == 0:
                    res += 1

            a>>=1
            b>>=1
            c>>=1
        return res        