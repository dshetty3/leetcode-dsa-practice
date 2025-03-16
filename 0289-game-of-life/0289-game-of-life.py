class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        # 1 - 0 - (< 2)         0 - 0       0
        # 1 - 1 - [2,3]         1 - 0       1
        # 1 - 0 - (> 3)         0 -  1      2
        # 0 - 1 - (== 3)        1 -  1      3
        
        m = len(board)
        n = len(board[0])

        def countNeighbours(r, c):
            nei = 0
            directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if ((nr == r and nc == c) or nr < 0 or nc < 0 or nr == m or nc == n):
                    continue
                if board[nr][nc] in [1,3]:
                    nei += 1
            return nei


        for r in range(m):
            for c in range(n):
                nei = countNeighbours(r, c)

                if board[r][c]:
                    if nei in [2,3]:
                        board[r][c] = 3
                else:
                    if nei == 3:
                        board[r][c] = 2
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == 1:
                    board[r][c] = 0
                elif board[r][c] in [2,3]:
                    board[r][c] = 1

