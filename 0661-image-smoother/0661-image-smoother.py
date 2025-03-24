class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """

        ROWS, COLS = len(img), len(img[0])
        

        res = [[0] * COLS for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                total = 0
                count = 0

                for i in range(r - 1, r + 2):
                    for j in range(c - 1, c + 2):
                        if i < 0 or i == ROWS or j < 0 or j == COLS:
                            continue
                        total += img[i][j]
                        count += 1
                res [r][c] = total // count
        return res


        