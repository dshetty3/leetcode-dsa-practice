class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        prev = -10 ** 9
        for i, n in enumerate(nums):
            if n == 1:
                if i - prev <= k:
                    return False
                prev = i
        return True
        