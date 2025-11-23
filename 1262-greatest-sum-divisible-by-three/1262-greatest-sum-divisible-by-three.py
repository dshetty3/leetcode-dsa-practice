class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        a = [x for x in nums if x % 3 == 0]
        b = sorted([x for x in nums if x % 3 == 1] , reverse = True)
        c = sorted([x for x in nums if x % 3 == 2] , reverse = True)

        res = 0
        for cntb in (len(b) - 2, len(b) - 1, len(b)):
            if cntb >= 0:
                for cntc in(len(c) - 2, len(c) - 1, len(c)):
                    if cntc >= 0 and (cntb -cntc) % 3 == 0:
                        res = max(res, sum(b[:cntb]) + sum(c[:cntc]))
                       
        return res + sum(a)
        