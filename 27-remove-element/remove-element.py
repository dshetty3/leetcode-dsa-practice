class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """


        k = 0 #initialize to 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i] #swap, i will go ahead 
                k += 1
        return k
        