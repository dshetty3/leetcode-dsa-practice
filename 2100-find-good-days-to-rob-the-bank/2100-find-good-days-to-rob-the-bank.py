class Solution(object):
    def goodDaysToRobBank(self, security, time):
        """
        :type security: List[int]
        :type time: int
        :rtype: List[int]
        """

        # res = []

        # if time == 0: return security
        # p1, p2 = 0, 0

        # for i in range(1, len(security) - time):

        #     if security[i - 1] >= security[i]:
        #         p1 += 1
        #     else: p1 = 0

        #     if security[i + time - 1] <= security[i + time]:
        #         p2 += 1
        #     else: p2 = 0

        #     if i >= time and p1 >= time and p2 >= time:
        #         res.append(i)
        # return res

        pre = [0] * len(security)
        post = [0] * len(security)
        pos = 0

        for i in range(len(security) - 1):
            if i == 0 or security[i] > security[i - 1]:
                pos = i
            pre[i] = i - pos
        
        for j in range(len(security) - 1, -1, -1):
            if j == len(security) - 1 or security[j + 1] < security[j]:
                pos = j
            post[j] = pos - j
        
        res = []
        for i in range(len(pre)):
            if pre[i] >= time and post[i] >= time:
                res.append(i)
        return res
        