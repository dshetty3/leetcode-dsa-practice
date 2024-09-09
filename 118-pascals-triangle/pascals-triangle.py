class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        res = [[1]]


        for i in range(numRows - 1):   
            #1 row is res - outer loop
            temp = [0] + res[-1] + [0]
            rows= []
            for j in range(len(res[-1]) + 1):
                #previous row + 1 - inner loop
                rows.append(temp[j] + temp[j+1])
            res.append(rows)
        return res


        