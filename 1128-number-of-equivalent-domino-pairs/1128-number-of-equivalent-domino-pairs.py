class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:

        # count = 0
        # for i in range(len(dominoes) - 1):
        #     s1 = dominoes[i][0]
        #     s2 = dominoes[i][1]
        #     for j in range(i + 1, len(dominoes)):
        #         d1 = dominoes[j][0]
        #         d2 = dominoes[j][1]
        #         if (s1 == d1 and s2 == d2) or (s1 == d2 and s2 == d1):
        #             count += 1
        # return count

        count = [0] * 100
        res = 0
        for i, j in dominoes:
            val = i * 10 + j if i <= j else j * 10 + i
            res += count[val]
            count[val] += 1
        return res


        