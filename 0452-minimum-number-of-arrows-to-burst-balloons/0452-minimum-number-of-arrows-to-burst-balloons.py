class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        arrow = 1

        points.sort()
        prevEnd = points[0][1]
        for i in range(1, len(points)):
            if prevEnd < points[i][0]:
                arrow += 1
                prevEnd = points[i][1]
            else:
                prevEnd = min(prevEnd, points[i][1])
        return arrow

        