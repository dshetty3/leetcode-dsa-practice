class Solution(object):
    def minTime(self, skill, mana):
        """
        :type skill: List[int]
        :type mana: List[int]
        :rtype: int
        """
        m = len(skill)
        n = len(mana)

        times = [0] * m
        for j in range(n):
            curr_time = 0
            for i in range(m):
                curr_time = max(curr_time, times[i]) + skill[i] * mana[j]
            times[m - 1] = curr_time
            for i in range(m - 2, -1, -1):
                times[i] = times[i + 1] - skill[i + 1] * mana[j]
        return times[m - 1]

        