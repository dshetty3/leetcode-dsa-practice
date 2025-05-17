class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        length = len(board)
        board.reverse()

        def intToPost(square):
            row = (square  - 1) // length
            col = (square - 1) % length
            if row % 2:
                col = length - 1 - col
            return [row,col]


        #How to write bfs
        q = deque()
        q.append([1, 0])
        visit = set()

        while q:
            square, moves = q.popleft()

            for i in range(1, 7):
                nextSquare = square + i
                r, c = intToPost(nextSquare)
                if board[r][c] != -1:
                    nextSquare = board[r][c]
                if nextSquare == length * length:
                    return moves + 1
                if nextSquare not in visit:
                    visit.add(nextSquare)
                    q.append([nextSquare, moves + 1])
        return -1

        