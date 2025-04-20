class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        
        m = len(mat)
        n = len(mat[0])
        q = deque()
        directions = [(1,0), (0,1),(-1,0),(0,-1)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = '*'
        
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                if 0 <= row < m and 0 <= col < n and mat[row][col] == '*':
                    mat[row][col] = 1 + mat[r][c]
                    q.append((row, col))
        return mat
        
       