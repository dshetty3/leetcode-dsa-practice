class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """

        ROWS = len(matrix)
        COLS = len(matrix[0])

        self.sumMatrix = [[0] * (COLS + 1) for c in range(ROWS + 1)]
        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.sumMatrix[r] [c + 1]
                self.sumMatrix[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """

        r1 = row1 + 1
        c1 = col1 + 1
        r2 = row2 + 1
        c2 = col2 + 1

        bottomRight = self.sumMatrix[r2][c2]
        above = self.sumMatrix[r1 - 1][c2]
        left = self.sumMatrix[r2][c1 - 1]
        topLeft = self.sumMatrix[r1 - 1][c1 - 1]

        return bottomRight - above - left + topLeft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)