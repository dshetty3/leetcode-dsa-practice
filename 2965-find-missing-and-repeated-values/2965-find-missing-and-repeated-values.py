class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        freq = {}

        for r in grid:
            for num in r:
                freq[num] = freq.get(num,0) + 1

        for num in range(1, n * n + 1):
            if num not in freq:
                missing = num
            elif freq[num] == 2:
                repeat = num 

        return [repeat, missing]     