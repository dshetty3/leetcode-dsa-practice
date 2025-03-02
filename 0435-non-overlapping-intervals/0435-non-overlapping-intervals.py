class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1] # take the first interval's end value and start the loop from second interval

        for start, end in intervals[1:]:
            if start >= prevEnd: # this edge case - not overlapping - compare w next values start
                prevEnd = end 
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res

        