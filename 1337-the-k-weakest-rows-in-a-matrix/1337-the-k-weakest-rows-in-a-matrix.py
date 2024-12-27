class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        res = []

        for i in range(len(mat[0])):
            for j in range(len(mat)):
                if mat[j][i] == 0 and j not in res:
                    res.append(j)
                    k -= 1
                    if not k:
                        return res
        
        for i in range(len(mat)):
            if i not in res:
                res.append(i)
                k -= 1
                if not k:
                    return res
        return res

        