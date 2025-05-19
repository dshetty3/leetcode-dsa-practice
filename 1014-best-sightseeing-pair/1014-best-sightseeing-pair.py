class Solution(object):
    def maxScoreSightseeingPair(self, values):
        """
        :type values: List[int]
        :rtype: int
        """

        max_score = 0
        max_left_score = [0] * len(values)
        max_left_score[0] = values[0]

        

        for i in range(1, len(values)):
            curr_right_score = values[i] - i
            max_score = max(max_score, max_left_score[i - 1] + curr_right_score)
            curr_left_score = values[i] + i
            max_left_score[i] = max(max_left_score[i - 1], curr_left_score)
        return max_score


        