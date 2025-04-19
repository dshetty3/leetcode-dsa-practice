class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        nums.sort()

        def helper(val):
            l = 0
            r = len(nums) - 1
            res = 0

            while l < r:
                if nums[l] + nums[r] < val:
                    res += r - l
                    l += 1
                else:
                    r -= 1
            return res

        return helper(upper + 1) - helper(lower)


        

