class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """

        x = 0

        for op in operations:
            if op[0] == '+' or op[2] == '+':
                x += 1
            else:
                x -= 1
        return x


        