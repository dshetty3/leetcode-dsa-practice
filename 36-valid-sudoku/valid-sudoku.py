class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        square = collections.defaultdict(set)

        for r in range(9): #rows
            for c in range(9): #col

                if board[r][c] == ".":
                    continue
                if (board[r][c] in row[r] or 
                    board[r][c] in col[c] or 
                    board[r][c] in square[(r//3,c//3)]):
                    return False
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                square[(r//3,c//3)].add(board[r][c])
        return True
            
