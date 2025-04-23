class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        def digitSum(n):
            s = 0
            while n:
                s += n % 10
                n //= 10
            return s

        mapSum = {}
        maxInt = 0
        count = 0

        for i in range(1, n + 1):
            x = digitSum(i)
            mapSum[x] = mapSum.get(x, 0) + 1
            maxInt = max(maxInt, mapSum[x])

        for v in mapSum.values():
            if v == maxInt:
                count += 1
        return count

        



        