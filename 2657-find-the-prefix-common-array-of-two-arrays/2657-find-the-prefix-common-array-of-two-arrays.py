class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """

        res = [0] * len(A)
        for i in range(len(A)):
            count = 0

            for a in range(i + 1):
                for b in range(i + 1):

                    if A[a] == B[b]:
                        count += 1
                        break
            res[i] = count
        return res


        return res
        