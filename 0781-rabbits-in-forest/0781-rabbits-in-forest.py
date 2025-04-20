class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """

        count = Counter(answers)

        total = 0
        for c in count.keys():
            total += ((count[c] + c) // (c + 1) ) * (c + 1)
        return total        