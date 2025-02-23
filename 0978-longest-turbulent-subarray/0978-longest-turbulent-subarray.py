class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        l, r = 0, 1
        res = 1
        prev = ""
        while r < len(arr):
            if arr[r - 1] > arr[r] and prev != '>':
                res = max(res, r - l + 1)
                r += 1
                prev = '>'
            elif arr[r - 1] < arr[r] and prev != '<':
                res = max(res, r - l + 1)
                r += 1
                prev = '<'
            else:
                r = r + 1 if arr[r] == arr[r - 1] else r
                prev = ""
                l = r - 1
        return res
        