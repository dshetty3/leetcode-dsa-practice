class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        if not mat or not mat[0]: return []

        res = []
        ROWS = len(mat)
        COLS = len(mat[0])

        r = 0
        c = 0

        direction = 1

        while r < COLS and c < ROWS:
            res.append(mat[r][c])

            new_row = r + (-1 if direction == 1 else 1)
            new_col = c + (1 if direction == 1 else -1)


            if new_row < 0 or new_row == COLS or new_col < 0 or new_col == ROWS:
                if direction:

                    r += (c == ROWS - 1)
                    c += (c < ROWS - 1)
                
                else:

                    c += (r == COLS - 1)
                    r += (r < COLS - 1)
                
                direction = 1 - direction
            
            else:
                r = new_row
                c = new_col

        return res
        