class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        nums.sort()
        for i in range(len(nums) - 2):
            k = i + 2
            for j in range(i + 1, len(nums) - 1):
                if(nums[i] != 0):
                    while(k < len(nums) and nums[i] + nums[j] > nums[k]):
                        k+= 1
                    count += k - j - 1
        return count

        