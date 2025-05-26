class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = {}
        res = []

        for n in nums:
            if n % 2 == 0:
                if n not in count:
                    count[n] = 1
                else:
                    count[n] += 1
        
        if len(count) == 0: return -1
        else:
            max_even = max(count.values())
            for freq, val in count.items():
                if val == max_even:
                    res.append(freq)
            return min(res)

        