class Solution(object):
    def checkValidCuts(self, n, rectangles):
        """
        :type n: int
        :type rectangles: List[List[int]]
        :rtype: bool
        """

        x = [ (r[0], r[2]) for r in rectangles]
        y = [ (r[1], r[3]) for r in rectangles]

        x.sort()
        y.sort()

        def countNonoverlapping(intervals):
            count = 0
            prevEnd = - 1
            for start, end in intervals:
                if prevEnd <= start:
                    count += 1
                prevEnd = max(prevEnd, end)
            return count
        

        return max(countNonoverlapping(x),
        countNonoverlapping(y)) >= 3
        
        