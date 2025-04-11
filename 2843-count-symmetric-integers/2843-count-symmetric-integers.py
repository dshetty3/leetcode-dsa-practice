class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        def isSymmtric(num):
            
            s = str(num)
            length = len(s)

            if length % 2 != 0:
                return False
            
            half = length // 2
            left_half = sum(int(d) for d in s[:half])
            right_half = sum(int(d) for d in s[half:])

            return left_half == right_half

        count = 0
        for n in range(low, high + 1):
            if isSymmtric(n):
                count += 1
        return count

       
            

        