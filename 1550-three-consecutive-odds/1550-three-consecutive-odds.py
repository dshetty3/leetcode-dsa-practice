class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """


        curr_count = 0
        max_count = 0

        for n in arr:
            if n % 2 != 0:
                curr_count += 1
                max_count = max(max_count, curr_count)
            else:
                curr_count = 0
        
        return max_count > 2

        