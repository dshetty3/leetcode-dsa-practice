class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        freq_map = Counter(nums)
        max_length = 0

        for n in freq_map:
            if n + 1 in freq_map:
                curr_length = freq_map[n] + freq_map[n + 1]
                max_length = max(max_length, curr_length)
        return max_length
        