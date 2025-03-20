class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """

        arr2.sort()
        count = 0
        for n in arr1:
            l = 0
            r = len(arr2)
            while l < r:
                m = (l + r) // 2
                if abs(arr2[m] - n) <= d:
                    count -= 1
                    break
                elif arr2[m] > n:
                    r = m
                elif arr2[m] < n:
                    l = m + 1
            count += 1
        return count
            