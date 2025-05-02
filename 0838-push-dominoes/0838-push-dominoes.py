class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """

        left = []
        right = []
        INF = 10 ** 20
        curr = INF
        for d in dominoes:
            if d == 'R':
                curr = 0
            elif d == 'L':
                curr = INF
            else:
                curr += 1
            curr = min(curr, INF)   
            left.append(curr)

        curr = INF
        for d in dominoes[::-1]:
            if d == 'L':
                curr = 0
            elif d == 'R':
                curr = INF
            else:
                curr += 1
            curr = min(curr, INF)
            right.append(curr)   
        right.reverse()

        res = []
        for i in range(len(dominoes)):
            if left[i] == right[i]:
                res.append('.')
            elif left[i] > right[i]:
                res.append('L')
            else:
                res.append('R')
        return "".join(res)     





        