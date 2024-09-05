class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        seen = set()
        #curr has be string 
        curr = str(n)

        while curr not in seen:
            seen.add(curr)
            sum = 0
            for i in curr:
                i = int(i)
                sum += i**2
            if sum == 1: 
                return True
            curr = str(sum)

        return False
        