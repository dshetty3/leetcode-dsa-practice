class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        num1 = ''
        res1 = []

        for n in num:
            num1 += str(n)

        res = int(num1) + k
        for n in str(res):
            res1.append(int(n))
        return res1       