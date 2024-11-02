class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        n = 3
        row = [0] * n
        cols = [0] * n
        leftDiagonal, rightDiagonal = 0, 0

        for index, move in enumerate(moves):
            i, j = move
            sign = 1 if index % 2 == 0 else -1

            row[i] += sign
            cols[j] += sign
            if i == j:
                rightDiagonal += sign
            if i + j == n - 1:
                leftDiagonal += sign
            if abs(row[i]) == n or abs(cols[j]) == n or abs(leftDiagonal) == n or abs(rightDiagonal) == n:
                return 'A' if sign is 1 else 'B'
        return 'Draw' if len(moves) == (n*n) else 'Pending'


        




        