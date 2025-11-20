class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        res = 0
        intervals.sort(key=lambda i: (i[1], -i[0]))
        p1, p2 = -1, -1

        for l, r in intervals:
            if p2 < l:
                res += 2
                p1, p2 = r - 1, r
            elif p1 < l:
                res += 1
                p1, p2 = p2, r 
        return res
            
        