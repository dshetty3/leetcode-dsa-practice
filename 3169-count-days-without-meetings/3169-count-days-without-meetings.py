class Solution(object):
    def countDays(self, days, meetings):
        """
        :type days: int
        :type meetings: List[List[int]]
        :rtype: int
        """


        meetings.sort()
        prev_end = 0

        for start, end in meetings:
            start = max(start, prev_end + 1)
            length = end - start + 1
            days -= max(length, 0)
            prev_end = max(prev_end, end)
        return days


        