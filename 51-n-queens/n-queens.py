class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        col = set()
        posD = set() #r + c
        negD = set() #r - c

        res = []
        board = [["."] * n for i in range(n)]

        def backtracking(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col or (r+c) in posD or (r-c) in negD:
                    continue
                
                col.add(c)
                posD.add(r + c)
                negD.add(r - c)
                board[r][c] = "Q"

                backtracking(r + 1)

                col.remove(c)
                posD.remove(r + c)
                negD.remove(r - c)
                board[r][c] = "."
        backtracking(0)
        return res


        