class Spreadsheet(object):

    def __init__(self, rows):
        """
        :type rows: int
        """
        self.mapp = {}
        

    def setCell(self, cell, value):
        """
        :type cell: str
        :type value: int
        :rtype: None
        """
        self.mapp[cell] = value
        

    def resetCell(self, cell):
        """
        :type cell: str
        :rtype: None
        """
        self.mapp[cell] = 0

    def getValue(self, formula):
        """
        :type formula: str
        :rtype: int
        """
        formula = formula[1:]
        for i in range(len(formula)):
            if formula[i] == "+":
                s1, s2 = formula[:i], formula[i + 1:]
                left = self.mapp.get(s1,0) if s1[0].isupper() else int(s1)
                right = self.mapp.get(s2,0) if s2[0].isupper() else int(s2)
                return left + right
        return 0

        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)