class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res = []
        count = {}
        for n in nums:
            if n in count:
                count[n] = count.get(n) + 1
            else:
                count[n] = 1
            if count[n] == 2:
                res.append(n)
        return res

        