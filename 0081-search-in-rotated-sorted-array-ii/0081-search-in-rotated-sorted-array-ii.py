class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        # n = len(nums)
        # l = 0
        # r = len(nums) - 1

        # while l <= r:
        #     m = (l + r) // 2
        #     if nums[m] > nums[r]:
        #         l += 1
        #     else:
        #         r = m
        
        # min_i = l
        # if min_i == 0:
        #     l = 0
        #     r = n - 1
        # elif target > nums[0] and target <= nums[min_i - 1]:
        #     l = 0
        #     r = min_i - 1
        # else:
        #     l = min_i
        #     r = n - 1
        
        # while l <= r:
        #     m = (l + r) // 2
        #     if num[m] == target:
        #         return True
        #     elif nums[m] < target:
        #         l = m + 1
        #     else:
        #         r = m - 1
        # return False


        n = len(nums)
        l = 0
        r = n - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m - 1
            # else:
            #     r -= 1
            

        min_i = l

        if min_i == 0:
            l, r = 0, n - 1
        elif target >= nums[0] and target <= nums[min_i - 1]:
            l, r = 0, min_i - 1
        else:
            l, r = min_i, n - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return True
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return False
            
            
        
        