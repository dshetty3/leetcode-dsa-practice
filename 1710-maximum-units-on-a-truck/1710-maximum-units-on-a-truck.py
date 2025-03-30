class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """

        boxTypes.sort(key = lambda x : -x[1])
        capacity = 0

        for box, units in boxTypes:
            if truckSize > box:
                truckSize -= box
                capacity += box * units
            else:
                capacity += truckSize * units
                break
        return capacity


        