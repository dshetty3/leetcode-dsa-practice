class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """

        cache = [0] * len(questions)

        def backtrack(i):
            if i >= len(questions):
                return 0
            if cache[i]:
                return cache[i]
            

            point, skip = questions[i]

            cache[i] = max (backtrack(i + 1),
            point + backtrack(i + 1 + skip))
            return cache[i]

        return backtrack(0)

        