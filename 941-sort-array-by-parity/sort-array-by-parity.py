class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # nums.sort(key = lambda x: x% 2)
        # return nums

        even = []
        odd = []
        for n in nums:
            if n % 2 == 0:
                even.append(n)
            else:
                odd.append(n)
        return even + odd



        