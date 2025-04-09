class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        visit = set()
        for n in nums:
            if n > k:
                visit.add(n)
            elif n < k:
                return -1
        return len(visit)



        