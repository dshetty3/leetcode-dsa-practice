class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1_c = nums1[:m]
        p1, p2 = 0,0
        for p in range(m+n):
            if p2 >=n or (p1 < m and nums1_c[p1] <= nums2[p2]):
                nums1[p] = nums1_c[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1

        