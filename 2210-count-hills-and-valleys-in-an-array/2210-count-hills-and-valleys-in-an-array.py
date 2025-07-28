class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        v = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                v.append(nums[i])
        

        count = 0
        for i in range(1, len(v) - 1):
            if (v[i] > v[i - 1] and v[i] > v[i + 1]) or (v[i] < v[i - 1] and v[i] < v[i + 1]):
                count += 1
        return count
        