class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """


        for i in range(1, n):
            j = n - i
            if "0" not in str(i) + str(j):
                return [i, j]
        return []
        