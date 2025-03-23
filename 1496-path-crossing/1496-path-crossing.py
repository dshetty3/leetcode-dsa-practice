class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        directions = {
        "N" : (0, 1),
        "S" : (0, -1),
        "E" : (1, 0),
        "W" : (-1, 0)
        }

        x, y = 0, 0
        pathSet = set()

        for c in path:
            pathSet.add((x,y))
            dx, dy = directions[c]
            x, y = x + dx, y + dy
            if (x,y) in pathSet:
                return True
        return False




        