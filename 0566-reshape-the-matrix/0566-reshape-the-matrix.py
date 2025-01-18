class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        flat = []
        for i in mat:
            flat += i
        if r * c != len(flat):
            return mat
        mat = []
        for j in range(0,len(flat), c):
            mat.append(flat[j:j+c])
        return mat
        