class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """ 
        # A, B = nums1, nums2
        # total = len(nums1) + len(nums2)
        # half = total // 2

        # if len(B) < len(A):
        #     A, B = B, A

        # l, r = 0, len(A) - 1
        # while True:
        #     i = (l + r) // 2
        #     j = half - i - 2

        #     Aleft = A[i] if i >= 0 else float("-infinity")
        #     Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
        #     Bleft = B[j] if j >= 0 else float("-infinity")
        #     Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

        #     if Aleft <= Bright and Bleft <= Aright:
        #         if total % 2:
        #             return min(Aright, Bright)
        #         return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
        #     elif Aleft > Bright:
        #         r = i - 1
        #     else:
        #         l = i + 1

        total = len(nums1) + len(nums2)
        half = total // 2

        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        l, r = 0, len(nums1) - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2

            nums1Left = nums1[i] if i >= 0 else float("-inf")
            nums1Right = nums1[i + 1] if (i + 1) < len(nums1) else float("inf")
            nums2Left = nums2[j] if j >= 0 else float("-inf")
            nums2Right = nums2[j + 1] if (j + 1) < len(nums2) else float("inf")


            if nums1Left <= nums2Right and nums2Left <= nums1Right:
                if total % 2:
                    return min(nums1Right, nums2Right)
                else:
                    return (max(nums1Left, nums2Left) + min(nums1Right, nums2Right)) / 2.0
            elif nums1Left > nums2Right:
                r = i - 1
            else:
                l = i + 1

        
                    





        