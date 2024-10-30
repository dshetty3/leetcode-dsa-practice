class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        m = len(matrix)
        n = len(matrix[0])

        if m != n:
            new = [[0] * m for _ in range(n)]
            for i in range(m):
                for j in range(n):
                    new[j][i] = matrix[i][j]
            return new


        for i in range(n):
            for j in range(i + 1, m):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix
        