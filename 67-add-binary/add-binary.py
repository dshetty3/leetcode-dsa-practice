class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        a, b = int(a,2), int(b,2)
        
        while b:
            no_carry = a ^ b
            carry = (a & b) << 1
            a, b = no_carry, carry
        return bin(a)[2:] #remove the 0b
        