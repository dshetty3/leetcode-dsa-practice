class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        window = set()
        l = 0


        for i in range(len(nums)):
            #extra edge case - remove elements from left 
            if (i - l) > k:
                window.remove(nums[l])
                l += 1
            if nums[i] in window:
                return True
            window.add(nums[i])
        return False
        