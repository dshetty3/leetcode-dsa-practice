class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        arr.sort(reverse = True)
        for n in arr:
            if arr.count(n) == n:
                return n
        return -1
        