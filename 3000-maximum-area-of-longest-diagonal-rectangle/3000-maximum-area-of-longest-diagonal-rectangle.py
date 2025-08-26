class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """

        max_dia_length = 0
        max_area = 0
        for l, w in dimensions:
            dia_length = l * l + w * w
            area = l * w
            if dia_length > max_dia_length:
                max_dia_length = dia_length
                max_area = area
            elif dia_length == max_dia_length:
                max_area = max(max_area, area)
        return max_area
        