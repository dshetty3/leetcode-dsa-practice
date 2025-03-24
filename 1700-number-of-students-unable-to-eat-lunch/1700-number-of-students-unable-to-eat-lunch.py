class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """

        count = Counter(students)
        res = len(students)

        for s in sandwiches:
            if count[s] > 0:
                res -= 1
                count[s] -= 1
            else:
                return res
        return res


        

        