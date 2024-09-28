class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """

        sorted_scores = sorted(score, reverse=True)

        res = [""] * len(score)

        for i in range(len(score)):
            place = sorted_scores.index(score[i]) + 1

            if place == 1:
                res[i] = "Gold Medal"
            elif place == 2:
                res[i] = "Silver Medal"
            elif place == 3:
                res[i] = "Bronze Medal"
            else:
                res[i] = str(place)

        return res




        