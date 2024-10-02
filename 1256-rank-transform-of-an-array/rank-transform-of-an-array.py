class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        nums_to_rank = {}

        nums = sorted(set(arr))
        rank = 1

        for num in nums:
            nums_to_rank[num] = rank
            rank += 1
        
        for i in range(len(arr)):
            arr[i] = nums_to_rank[arr[i]]
        return arr
