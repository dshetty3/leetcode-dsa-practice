class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if len(nums) == 1:
            return nums
        
        # p = nums[-1]
        # left = [x for x in nums[:-1] if x < p]
        # right = [x for x in nums[:-1] if x >= p]

        # left = self.sortArray(left)
        # right = self.sortArray(right)

        # return left + [p] + right

        m = len(nums) // 2
        L = nums[:m]
        R = nums[m:]

        L = self.sortArray(L)
        R = self.sortArray(R)

        l, r = 0, 0

        len_l = len(L)
        len_r = len(R)

        sorted_arr = [0] * len(nums)
        i = 0

        while l < len_l and r < len_r:
            if L[l] < R[r]:
                sorted_arr[i] = L[l]
                l += 1
            else:
                sorted_arr[i] = R[r]
                r += 1
            i += 1

        while l < len_l:
            sorted_arr[i] = L[l]
            l += 1
            i += 1

        while r < len_r:
            sorted_arr[i] = R[r]
            r += 1
            i += 1        
        return sorted_arr