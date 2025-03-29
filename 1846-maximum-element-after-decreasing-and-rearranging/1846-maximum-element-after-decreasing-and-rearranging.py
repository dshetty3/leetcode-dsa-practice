class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        prev_element = 0

        for n in arr:
            prev_element = min(prev_element + 1, n)
        return prev_element
        