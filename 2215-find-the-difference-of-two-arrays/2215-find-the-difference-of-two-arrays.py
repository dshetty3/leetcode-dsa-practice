class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        res = []

        n1 = set(nums1)
        n2 = set(nums2)
        common = n1.intersection(n2)

        res1 = []
        for n in n1:
            if n not in common:
                res1.append(n)
        res.append(res1)

        res2 = []
        for n in n2:
            if n not in common:
                res2.append(n)
        res.append(res2)
        return res
        