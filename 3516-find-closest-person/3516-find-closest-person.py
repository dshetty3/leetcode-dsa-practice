class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        dist_x = abs(z - x)
        dist_y = abs(z - y)

        if dist_x < dist_y:
            return 1
        elif dist_y < dist_x:
            return 2
        else:
            return 0

        