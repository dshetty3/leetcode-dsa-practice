class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        
        
        count = Counter()
        for r in grid:
            count[tuple(r)] += 1
        

        res = 0
        for i in range(len(grid)):
            temp = []
            for j in range(len(grid)):
                temp.append(grid[j][i])
            
            res += count[tuple(temp)]
        
        return res
        
            


        