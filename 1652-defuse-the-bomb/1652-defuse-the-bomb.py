class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """

        res = [0] * len(code)

        

        for i in range(len(code)):
            if k > 0:
                for j in range(i + 1, i + 1 + k):
                    res[i] += code[j % len(code)]
            elif k < 0:
                for j in range(i - 1, i - 1 - abs(k), -1):
                    res[i] += code[j % len(code)]
        return res
        # l = 0
        # curr = 0
        # for r in range(len(code) + k):
        #     curr += code[r % len(code)]

        #     if r - l + 1 > abs(k):
        #         curr -= code[l % len(code)]
        #         l = (l + 1) % len(code)

        #     if r - l + 1 == abs(k):
        #         if k > 0:
        #             res[(l - 1) % len(code)] = curr
        #         if k < 0:
        #             res[(r + 1) % len(code)] = curr
        # return res



        