class Solution(object):
    def isPossibleToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        nums1 = []
        nums2 = []
        
        for num in nums:
            if num not in nums1:
                nums1.append(num)
            elif num not in nums2:
                nums2.append(num)
            else:
                return False
        
        return True
        