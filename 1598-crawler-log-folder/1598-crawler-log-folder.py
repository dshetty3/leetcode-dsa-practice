class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """

        count = 0
        for log in logs:
            if log == './':
                continue
            elif log == '../':
                if count > 0:
                    count -= 1
            else:
                count += 1
        return count
        