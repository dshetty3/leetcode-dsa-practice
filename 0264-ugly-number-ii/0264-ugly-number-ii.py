class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        nums = set()
        nums.add(1)

        curr = 1
        for i in range(n):
            curr = min(nums)
            nums.remove(curr)

            nums.add(curr * 2)
            nums.add(curr * 3)
            nums.add(curr * 5)

        return curr


        