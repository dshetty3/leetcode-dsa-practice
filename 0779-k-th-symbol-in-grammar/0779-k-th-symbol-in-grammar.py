class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        l = 1
        r = 2 ** (n - 1)
        curr = 0

        for i in range(n - 1):
            mid = (l + r) // 2
            if k <= mid:
                r = mid
            else:
                l = mid + 1
                curr = 0 if curr else 1
        return curr


        