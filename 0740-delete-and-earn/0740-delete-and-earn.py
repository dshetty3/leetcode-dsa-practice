class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = Counter(nums)


        nums = sorted(list(set(nums)))
        earn1, earn2 = 0, 0

        for i in range(len(nums)):
            currEarn = nums[i] * count[nums[i]]
            if i > 0 and nums[i] == nums[i - 1] + 1:
                temp = earn2
                earn2 = max(earn2, currEarn + earn1)
                earn1 = temp
            else:
                temp = earn2
                earn2 = currEarn + earn2
                earn1 = temp
        return earn2


        