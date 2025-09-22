class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        frequencies = {}
        for n in nums:
            if n in frequencies:
                frequencies[n] += 1
            else:
                frequencies[n] = 1
        
        max_frequency = 0
        for f in frequencies.values():
            max_frequency = max(max_frequency, f)
        
        frequency_max = 0
        for f in frequencies.values():
            if f == max_frequency:
                frequency_max += 1
        
        return frequency_max * max_frequency
        