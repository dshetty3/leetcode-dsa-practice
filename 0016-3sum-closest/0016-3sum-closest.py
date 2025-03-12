class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        closest = float("inf")

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]: continue

            l, r  = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]

                if abs(threeSum - target) < abs(closest - target):
                    closest = threeSum

                if threeSum == target:
                    return threeSum
                elif threeSum > target:
                    r -= 1
                else:
                    l += 1
        return closest

        