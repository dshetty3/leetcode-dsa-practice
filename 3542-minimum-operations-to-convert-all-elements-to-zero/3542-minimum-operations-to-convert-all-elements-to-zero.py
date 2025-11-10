class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        heap = []
        res = 0
        for n in nums:
            while heap and heap[-1] > n:
                heap.pop()
            if n == 0:
                continue
            if not heap or heap[-1] < n:
                res += 1
                heap.append(n)
        return res
        