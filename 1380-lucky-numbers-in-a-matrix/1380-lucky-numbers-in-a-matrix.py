class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        lucky = []

        for i in range(len(matrix)):
            min = matrix[i][0]
            max = 0
            min_i = 0

            for j in range(len(matrix[i])):
                if matrix[i][j] < min:
                    min = matrix[i][j]
                    min_i =j
            for k in range(len(matrix)):
                if max < matrix[k][min_i]:
                    max = matrix[k][min_i]
            if max == min:
                lucky.append(max)

        return lucky
        