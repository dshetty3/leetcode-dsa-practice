class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """

        max_idx = max(max(seats), max(students)) + 1
        count_seats = [0] * 101
        count_students = [0] * 101

        for c in seats:
            count_seats[c] += 1
        for c in students:
            count_students[c] += 1

        i, j = 0, 0
        res = 0
        remain = len(students)

        while remain:
            if count_seats[i] == 0:
                i += 1
            if count_students[j] == 0:
                j += 1
            if count_seats[i] and count_students[j]:
                res += abs(i - j)
                count_seats[i] -= 1
                count_students[j] -= 1
                remain -= 1
        return res

        